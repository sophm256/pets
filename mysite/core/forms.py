from django import forms

from django.contrib.auth.forms import UserCreationForm
from mysite.core.models import CustomUser, Pet


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required')
    phone = forms.CharField(max_length=15, required=False, help_text='Optional')
    profile_image = forms.ImageField(required=False, help_text='Optional')
    class Meta:
        model = CustomUser
        fields = ('username', 'profile_image', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


class PetProfileForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('profile_image','name','pet_type', 'remarks', 'date_last_seen', 'time_last_seen', 'last_known_location')
        widgets = {
            'remarks': forms.Textarea(
                attrs={'cols': 50, 'rows': 10, 
                    'placeholder': 'Write your pet description and any special instructions here! Include how they should contact you.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet_type'].widget.attrs.update({'placeholder': 'For example, "Dog" or "Cat"'})
        self.fields['date_last_seen'].widget.attrs.update({'id': 'date_last_seen', 'placeholder':'For example, "1/20/2019"'})
        self.fields['time_last_seen'].widget.attrs.update({'id': 'time_last_seen', 'placeholder':'For example, "12:36 PM"'})
        self.fields["time_last_seen"].input_formats = ['%I:%M %p',]
        self.fields["time_last_seen"].format = '%I:%M %p'


class SearchForOwnerForm(forms.Form):
    search_by_username = forms.CharField(label='Search by Username', max_length = 150)