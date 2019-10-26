from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, blank=True)
    
    REQUIRED_FIELDS = ['email']

    class Meta(object):
    	unique_together=('email',)