from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from mysite.core.models import CustomUser
# Register your models here.

#admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(OSMGeoAdmin):
    #list_display = ('name', 'location')
    pass