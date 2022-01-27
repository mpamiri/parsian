from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
def home(req):
    return render(req,'home.html')
def contact_us(req):
    return render(req,'contact_us.html')
def occupational_medicine(req):
    return render(req,'occupational_medicine.html')
def services(req):
    return render(req,'services.html')
def login(req):
    form=UserCreationForm()
    if req.method == 'POST':
        form=UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(req,'login.html',context)
