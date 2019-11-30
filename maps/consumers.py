from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from mysite.core.models import TrackingCoord, StartStopTime, CustomUser, SearchPartyInstance, SearchPartyMembers
from django.contrib.gis.geos import fromstr
import datetime

class MapsConsumer(WebsocketConsumer):
    #coord_dict ={'alan':[[-87, 43]]}
    # def __init__(self):
    #     super().__init__()
    #     self.coord_dict ={'alan':[[-87, 43]]}

    # def addToDict(self, username, coord):
    #     if username in self.coord_dict:
    #         self.coord_dict[username].append(coord)
    #     else:
    #         self.coord_dict[username]= [coord]
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        message_type = text_data_json["message_type"]

        username = text_data_json['username']
        search_party_instance_id = text_data_json['search_party_instance_id']
        custom_user = CustomUser.objects.get(username=username)
        membership= SearchPartyMembers.objects.get(member=custom_user)
        js_timestamp = text_data_json['time_stamp']
        date_time = datetime.datetime.fromtimestamp(js_timestamp)

        if (message_type == 'coordinate'):
            coord = text_data_json['coord']
            longitude = coord[0]
            latitude = coord[1]
            
            # Add the coordinate to the TrackingCoord table
            my_point = fromstr(f'POINT({longitude} {latitude})', srid=4326)
            tracking_coord = TrackingCoord.objects.create(search_party_member=membership, my_point=my_point, date_time=date_time)
            tracking_coord.save()
        
        elif (message_type == 'start_tracking' or message_type == 'stop_tracking'):
            if (message_type == 'start_tracking'):
                start_or_stop_type = 1
            elif (message_type == 'stop_tracking'):
                start_or_stop_type = 2
            start_stop_time = StartStopTime.objects.create(search_party_member=membership, datetime_start_or_stop=date_time, start_or_stop_type=start_or_stop_type)
            start_stop_time.save()

        # Get all of the coordinates for that particular member from the database
        #TODO
        #TrackingCoord.objects.

        # self.addToDict(username,coord)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                #TODO 'coordinates': self.coord_dict[username]
                'coordinates': [4,5]
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        username = event['username']
       #TODO coordinates = event['coordinates']
        coordinates = event['coordinates']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': username,
        #TODO  'coordinates': coordinates
        'coordinates': coordinates     
        }))

    