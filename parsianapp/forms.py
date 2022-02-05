from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results
class registration(UserCreationForm):
    class meta:
        model=User
        fields=['username','password']


class summary_of_results(forms.ModelForm):
    
    class Meta:
        model = summary_of_results
        fields = '__all__'
