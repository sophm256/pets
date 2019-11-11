from django.urls import path
from . import views

urlpatterns = [
    path('', views.mymap_orig, name='mymap_orig'),
    path('<str:room_name>', views.mymap, name='mymap'),
    path('<str:room_name>/', views.mymap, name='mymap'),
]