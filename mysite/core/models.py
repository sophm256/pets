from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='user_images', blank=True)

    REQUIRED_FIELDS = ['email']

    class Meta(object):
    	unique_together=('email',)


class Pet(models.Model):
    profile_image = models.ImageField('Photo of Your Pet', upload_to='pet_images', blank=True)
    name = models.CharField('Name of Pet', max_length=15)
    pet_type = models.CharField(max_length=25)
    remarks = models.CharField(max_length=1000,blank=True)
    date_last_seen = models.DateField()
    time_last_seen = models.TimeField()
    last_known_location = models.CharField(max_length=25)
    owner = models.ForeignKey('CustomUser',on_delete=models.CASCADE)

    
class SearchPartyInstance(models.Model):
    owner = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    pet = models.ForeignKey('Pet',on_delete=models.CASCADE)

class SearchPartyMembers(models.Model):
    search_party_instance = models.ForeignKey('SearchPartyInstance', on_delete=models.CASCADE)
    member = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
   
class TrackingCoord(models.Model):
    search_party_member = models.ForeignKey('SearchPartyMembers', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    my_point = models.PointField(srid=4326) 

class StartStopTime(models.Model):
    search_party_member = models.ForeignKey('SearchPartyMembers', on_delete=models.CASCADE)
    datetime_start_or_stop = models.DateTimeField(default=timezone.now)
    start_or_stop_type = models.SmallIntegerField(choices=[(1,'start'),(2,'stop')])