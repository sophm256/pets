from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import CustomUser
from mysite.core.forms import SignUpForm, PetProfileForm


# @login_required
# def home(request):
#     return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'mysite/signup.html', {'form': form})

@login_required
def pet_profile_form(request):
    
    if request.method == "POST":
        form = PetProfileForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = CustomUser.objects.get(pk=request.user.id)
            pet.save()
           
            return redirect('home')
    else:
        form = PetProfileForm()
    return render(request, 'mysite/pet_profile_form.html', {'form': form})