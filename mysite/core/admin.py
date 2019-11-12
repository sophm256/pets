from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from mysite.core.models import CustomUser, Pet, SearchInstance, SearchPartyMembers, TrackingCoord, StartEndPeriod
# Register your models here.

#admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(OSMGeoAdmin):
    #list_display = ('name', 'location')
    pass

admin.site.register(Pet)
admin.site.register(SearchInstance)
admin.site.register(SearchPartyMembers)
admin.site.register(TrackingCoord)
admin.site.register(StartEndPeriod)