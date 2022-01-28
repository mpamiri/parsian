from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import registration
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
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
            user=form.cleaned_data.get('username')
            messages.success(req, 'account made succcessfuly for ' + user)
            return redirect('login')
    context={'form':form}
    return render(req,'register.html',context)
def login(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)

        if user is not None:
            login(req,user)
            return redirect('../manage)
        else:
            messages.info(req, 'username or password is incorect')
    return render(req,'login.html')
login_required(login_url='login')
def manage(req):
    return render(req,'manage.html')


def logout(req):
    logout(req)
    return redirect('../home')