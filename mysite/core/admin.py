from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from mysite.core.models import CustomUser, Pet, SearchPartyMembers, SearchPartyInstance, TrackingCoord, StartStopTime
# Register your models here.

#admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(OSMGeoAdmin):
    #list_display = ('name', 'location')
    pass

admin.site.register(Pet)
admin.site.register(SearchPartyMembers)
admin.site.register(SearchPartyInstance)
admin.site.register(TrackingCoord)
admin.site.register(StartStopTime)