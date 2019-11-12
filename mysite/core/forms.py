from django import forms
from django.contrib.auth.forms import UserCreationForm
from mysite.core.models import CustomUser, Pet


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=15, required=False, help_text='Optional.')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


class PetProfileForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('profile_image','name','pet_type', 'breed', 'age','gender')