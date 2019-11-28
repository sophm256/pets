from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import CustomUser, SearchPartyInstance, Pet, SearchPartyMembers
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
            return redirect('triage')
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
           
            # create search party instance
            my_pet = Pet.objects.get(pk=pet.pk)
            search_party_instance = SearchPartyInstance.objects.create(owner=pet.owner,pet=my_pet)
            search_party_instance.save()

            # add owner to the search party member list
            SearchPartyMembers.objects.create(search_party_instance=search_party_instance, member=pet.owner)
            return redirect('search_party_flyer', pk=search_party_instance.pk)
    else:
        form = PetProfileForm()
    return render(request, 'mysite/pet_profile_form.html', {'form': form})

@login_required
def triage(request):
    return render(request, 'mysite/triage.html', {})

@login_required
def search_party_flyer(request, pk):
    search_party_instance = SearchPartyInstance.objects.get(pk = pk)
    pet = search_party_instance.pet
    owner = search_party_instance.owner

    search_party_members = SearchPartyMembers.objects.filter(search_party_instance=pk)

    members=[]
    for person in search_party_members:
        members.append(person.member.username)

    if request.method == "POST":
        username = request.POST["adding_member"]
        # pk_instance = request[pk_instance]
        user = CustomUser.objects.get(username=username)
        
        search_party_members = SearchPartyMembers.objects.create(search_party_instance=search_party_instance, member=user)
        search_party_members.save()
        return redirect('mymap_slash', room_name=pk)
    return render(request, 'mysite/search_party_flyer.html', {"pet":pet, "owner":owner, "pk":pk, "members": members})