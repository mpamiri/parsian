from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results as Summary
from .forms import registration , summary_of_results
from django.contrib import messages
from django.contrib.auth import logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
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
            return redirect('../login')
    context={'form':form}
    return render(req,'register.html',context)
def login(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)

        if user is not None:
            auth_login(req,user)
            return redirect('../manage')
        else:
            messages.info(req, 'username or password is incorect')
    return render(req,'login.html')
@login_required(login_url='login')
def manage(req):
    return render(req,'manage.html')


@login_required(login_url='login')
def summary(req):
    work=Summary.objects.latest()
    code-work.work_code
    initial_dict = {
        work_code:code
    }
    form=summary_of_results(initial=initial_dict)
    context={'form':form}
    return render(req,'summary_of_results.html',context)
    
@require_POST
def addsummary(req):
    form=summary_of_results(req.POST)
    if form.is_valid():
        new_summary=form.save()
    return redirect('summary_of_results')


def logoutuser(req):
    logout(req)
    return redirect('../')