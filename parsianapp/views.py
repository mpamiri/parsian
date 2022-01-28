from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import registration
def home(req):
    return render(req,'home.html')
def contact_us(req):
    return render(req,'contact_us.html')
def occupational_medicine(req):
    return render(req,'occupational_medicine.html')
def services(req):
    return render(req,'services.html')
def register(req):
    form=registration()
    if req.method == 'POST':
        form=registration(req.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(req,'register.html',context)
def login(req):
    return render(req,'login.html')