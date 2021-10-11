from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from django.utils.translation import ugettext_lazy as _

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields =('username','email')
         
        