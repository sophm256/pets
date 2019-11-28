from django.urls import path
from . import views

urlpatterns = [
    path('', views.mymap_orig, name='mymap_orig'),
    path('<int:room_name>', views.mymap, name='mymap'),
    path('<int:room_name>/', views.mymap, name='mymap_slash'),
]