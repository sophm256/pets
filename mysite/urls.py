"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views as auth_views
from mysite.core import views as core_views

from mysite import views
from django.shortcuts import redirect
from maps import views as map_views
from chat import views as chat_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('maps', map_views.mymap_orig, name='mymap'),
    path('chat', chat_views.index, name='index'),
    path('maps/', include('maps.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('pet_profile_form/', core_views.pet_profile_form, name='pet_profile_form'),
    path('triage/', core_views.triage, name='triage'),
    path('search_party_flyer/<int:pk>/', core_views.search_party_flyer, name='search_party_flyer'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)