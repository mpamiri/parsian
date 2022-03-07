from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results,submit_company,disease
from .forms import registration, summary_of_results_form,submit_company_form,disease_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.views import generic
from . import forms, models


def home_view(req):
    return render(req, 'home.html')


def contact_us_view(req):
    return render(req, 'contact_us.html')


def occupational_medicine_view(req):
    return render(req, 'occupational_medicine.html')


def services_view(req):
    return render(req, 'services.html')


def register_view(req):
    form = registration()
    if req.method == 'POST':
        form = registration(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, 'account made succcessfuly for ' + user)
            return redirect('../login')
    context = {'form': form}
    return render(req, 'register.html', context)


def login_view(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)

        if user is not None:
            auth_login(req, user)
            return redirect('../manage')
        else:
            messages.info(req, 'username or password is incorect')
    return render(req, 'login.html')


@login_required(login_url='login')
def manage_view(req):
    return render(req, 'manage.html')


@login_required(login_url='login')
def submit_person_view(req):
    work=summary_of_results.objects.last()
    code_list=submit_company.objects.order_by('id')
    if work:
        code=work.examinations_code
    else:
        code=''
    initial_dict = {
        'examinations_code':code
        
    }
    form=summary_of_results_form(initial=initial_dict)
    context={'form':form,
    'code_list':code_list}
    return render(req,'summary_of_results.html',context)


@require_POST
def addperson_view(req):
    form = summary_of_results_form(req.POST)
    if form.is_valid():
        new_summary = form.save()
    return redirect('submit_person')


def logoutuser_view(req):
    logout(req)
    return redirect('../')


@login_required(login_url='login')
def company_view(req):
    form=submit_company_form()
    context={'form':form}
    return render(req, 'submit_company.html',context)


@require_POST
def addcompany_view(req):
    form=submit_company_form(req.POST)
    if form.is_valid():
        new_company=form.save()
    return redirect('submit_company')

@login_required(login_url='login')
def output_view(req):
    form=disease_form()
    code_list=submit_company.objects.order_by('id')
    context={'form':form,'code_list':code_list}
    return render(req,'output.html',context)

@require_POST
def adddisease_view(req):
    form=disease_form(req.POST)
    if form.is_valid():
        new_disease=form.save()
    return redirect('output')


@login_required(login_url='login')
def disease_code_view(req):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'company':company}
    return render(req, 'disease_code.html',context)

@login_required(login_url='login')
def open_docs_view(req):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'company':company}
    return render(req, 'open_docs.html',context)

@login_required(login_url='login')
def summary_of_examinations_view(req):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'company':company}
    return render(req, 'summary_of_examinations.html',context)

@login_required(login_url='login')
def problem_view(req):
    return render(req, 'problem.html')

@login_required(login_url='login')
def specialist_view(req):
    return render(req, 'specialist.html')

@login_required(login_url='login')
def graph_view(req):
    return render(req, 'graph.html')

@login_required(login_url='login')
def solo_output_view(req):
    return render(req, 'solo_output.html')

@login_required(login_url='login')
def input_view(req):
    return render(req, 'input.html')