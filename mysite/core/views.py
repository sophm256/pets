from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import CustomUser, SearchPartyInstance, Pet, SearchPartyMembers
from mysite.core.forms import SignUpForm, PetProfileForm, SearchForOwnerForm
from django.core.exceptions import ObjectDoesNotExist

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
def user_profile(request, pk):
   custom_user = CustomUser.objects.get(pk=pk) 
   return render(request, 'mysite/user_profile.html', {'custom_user':custom_user})

@login_required
def pet_profile_form(request):
    
    if request.method == "POST":
        form = PetProfileForm(request.POST)
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
    my_username = request.user.username
    my_custom_user = CustomUser.objects.get(username = my_username)
    my_pets = Pet.objects.filter(owner=my_custom_user)
    my_pets_and_search_party_instance =[]

    for my_pet in my_pets:
        my_search_party_instance = SearchPartyInstance.objects.get(owner=my_custom_user,pet=my_pet)
        my_pets_and_search_party_instance.append([my_pet, my_search_party_instance.pk])
    

    if request.method == 'POST':
        form = SearchForOwnerForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('search_by_username')
            custom_user = None
            pets_and_search_party_instance =[]
            try:
                
                custom_user = CustomUser.objects.get(username = username)
                pets = Pet.objects.filter(owner=custom_user)
                
                for pet in pets:
                    search_party_instance = SearchPartyInstance.objects.get(owner=custom_user,pet=pet)
                    pets_and_search_party_instance.append([pet,search_party_instance.pk])
                form = SearchForOwnerForm()
                found_owner = True
            except ObjectDoesNotExist:
                found_owner = False
            form_is_bound = "true"
            
            return render(request, 'mysite/triage.html', {'form': form,'found_owner': found_owner,'owner':custom_user, 'pets_and_search_party_instance':pets_and_search_party_instance, 'form_is_bound': form_is_bound, 'my_pets_and_search_party_instance': my_pets_and_search_party_instance })
    else:
        form = SearchForOwnerForm()
        form_is_bound = "false"
        return render(request, 'mysite/triage.html', {'form': form, 'form_is_bound': form_is_bound, 'my_pets_and_search_party_instance': my_pets_and_search_party_instance })

   

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