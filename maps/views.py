from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
import json

# Create your views here.
def mymap_orig(request):
   
    return render(request, 'maps/mymap_orig.html', {})


#IMPORTANT:Should we be marking it safe??
def mymap(request, room_name):
    return render(request, 'maps/mymap.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })