from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

from .models import Userprofile


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=('address',)