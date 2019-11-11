from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
   
    return render(request, 'mysite/index.html', {})

def user_profile(request):
   
    return render(request, 'mysite/user_profile.html', {})