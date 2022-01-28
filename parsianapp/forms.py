from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class registration(UserCreationForm):
    class meta:
        model=User
        fields=['username','password']