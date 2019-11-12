from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='images', blank=True)

    REQUIRED_FIELDS = ['email']

    class Meta(object):
    	unique_together=('email',)


class Pet(models.Model):
    profile_image = models.ImageField(upload_to='pet_images', blank=True)
    name = models.CharField(max_length=15)
    pet_type = models.CharField(max_length=25, help_text='For example, dog or cat')
    breed = models.CharField(max_length=25, blank=True)
    age = models.SmallIntegerField(blank=True, help_text='age in years')
    gender = models.CharField(max_length=1, blank=True, choices = [('M','male'),('F','female')])
    owner = models.ForeignKey('CustomUser',on_delete=models.SET_NULL, null=True)
    

class SearchInstance(models.Model):
    remarks = models.CharField(max_length=500,blank=True)
    date_last_seen = models.DateField()
    time_last_seen = models.TimeField()
    last_known_location = models.CharField(max_length=25)
    owner = models.ForeignKey('CustomUser',on_delete=models.SET_NULL, null=True)
    pet = models.ForeignKey('Pet', on_delete=models.SET_NULL, null=True)

class SearchPartyMembers(models.Model):
    search_instance = models.ForeignKey('SearchInstance', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
   
class TrackingCoord(models.Model):
    search_party_member = models.ForeignKey('SearchPartyMembers', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    my_point = models.PointField(srid=4326) 

class StartEndPeriod(models.Model):
    search_party_member = models.ForeignKey('SearchPartyMembers', on_delete=models.CASCADE)
    datetime_start_or_end = models.DateTimeField(default=timezone.now)
    start_or_end_type = models.SmallIntegerField # 1=start, 2=stop