from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json



class MapsConsumer(WebsocketConsumer):
    coord_dict ={'alan':[[-87, 43]]}
    # def __init__(self):
    #     super().__init__()
    #     self.coord_dict ={'alan':[[-87, 43]]}

    def addToDict(self, username, coord):
        if username in self.coord_dict:
            self.coord_dict[username].append(coord)
        else:
            self.coord_dict[username]= [coord]
    
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
        coord = text_data_json['coord']
        username = text_data_json['username']

        self.addToDict(username,coord)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'coordinates': self.coord_dict[username]
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        username = event['username']
        coordinates = event['coordinates']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': username,
            'coordinates': coordinates
        }))

    