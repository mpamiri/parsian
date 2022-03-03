from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results,submit_company,disease,examinations
from .forms import registration, summary_of_results_form,submit_company_form,disease_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.views import generic
from . import forms, models


def home(req):
    return render(req, 'home.html')


def contact_us(req):
    return render(req, 'contact_us.html')


def occupational_medicine(req):
    return render(req, 'occupational_medicine.html')


def services(req):
    return render(req, 'services.html')


def register(req):
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


def login(req):
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
def manage(req):
    return render(req, 'manage.html')


@login_required(login_url='login')
def summary(req):
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
def addsummary(req):
    form = summary_of_results_form(req.POST)
    if form.is_valid():
        new_summary = form.save()
    return redirect('summary_of_results')


def logoutuser(req):
    logout(req)
    return redirect('../')


@login_required(login_url='login')
def company(req):
    form=submit_company_form()
    context={'form':form}
    return render(req, 'submit_company.html',context)


@require_POST
def addcompany(req):
    form=submit_company_form(req.POST)
    if form.is_valid():
        new_company=form.save()
    return redirect('submit_company')

@login_required(login_url='login')
def occupational_disease(req):
    form=disease_form()
    code_list=submit_company.objects.order_by('id')
    context={'form':form,'code_list':code_list}
    return render(req,'occupational_diseases.html',context)

@require_POST
def adddisease(req):
    form=disease_form(req.POST)
    if form.is_valid():
        new_disease=form.save()
    return redirect('occupational_disease')


@login_required(login_url='login')
def disease_code(req):
    work=disease.objects.last()
    Summary=summary_of_results.objects.filter(examinations_code=work.examinations_code)
    company=submit_company.objects.filter(examinations_code=work.examinations_code)
    context={'summary':Summary,'company':company}
    return render(req, 'disease_code.html',context)

@login_required(login_url='login')
def open_docs(req):
    return render(req, 'open_docs.html')

@login_required(login_url='login')
def summary_of_examinations(req):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    models=examinations.objects.filter(examinations_code=code)
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    for model in models:
        for summary in Summary:
            if model.name != summary.name:
                if summary.left_ear_hearing == 'normal':
                    audio_normal='*'
                if summary.breathing_test == 'normal':
                    espiro_normal='*'
                if summary.color_vision == 'normal':
                    opto_normal='*'
                if summary.urine == 'normal':
                    test_normal='*'
                if summary.refer_to_specialist == 'none':
                    specialist_no_need='*'
                if summary.final_theory == 'belamane':
                    doctor_normal='*'
                if summary.final_theory  == 'taghir_shekl':
                    doctor_change='*'
                if summary.final_theory  == 'mashrot':
                    doctor_condition='*'
                if summary.final_theory  == 'comision':
                    doctor_comision='*'
                if summary.occupational_actions == 'darhal_peygiri':
                    specialist_invest='*'
                if summary.occupational_actions  == 'done':
                    specialist_done='*'
                else:
                    specialist_not_done='*' 
                    specialist_invest=''
                    specialist_done=''
                    doctor_comision=''
                    doctor_condition=''
                    doctor_change=''
                    doctor_normal=''
                    specialist_need='*'
                    specialist_no_need=''
                    test_not_normal='*'
                    test_normal=''
                    opto_not_normal='*'
                    opto_normal=''
                    espiro_not_normal='*'
                    espiro_normal=''
                    audio_not_normal='*'
                    audio_normal=''
                modelcreate=examinations.objects.create(
                audio_normal=audio_normal
                ,audio_not_normal=audio_not_normal
                ,espiro_normal=espiro_normal
                ,espiro_not_normal=espiro_not_normal
                ,opto_normal=opto_normal
                ,opto_not_normal=opto_not_normal
                ,test_normal=test_normal
                ,test_not_normal=test_not_normal
                ,examinations_code=code
                ,specialist_need=specialist_need
                ,specialist_no_need=specialist_no_need
                ,doctor_normal=doctor_normal
                ,doctor_change=doctor_change
                ,doctor_condition=doctor_condition
                ,doctor_comision=doctor_comision
                ,specialist_invest=specialist_invest
                ,specialist_done=specialist_done
                ,specialist_not_done=specialist_not_done
                ,name=summary.name
                ,age=summary.age
                ,job=summary.job
                ,harmful=summary.harmful_factors)
                modelcreate.save() 
    context={'summary':Summary,'company':company,'models':models}
    return render(req, 'summary_of_examinations.html',context)

@login_required(login_url='login')
def problem(req):
    return render(req, 'problem.html')

@login_required(login_url='login')
def specialist(req):
    return render(req, 'specialist.html')

@login_required(login_url='login')
def graph(req):
    return render(req, 'graph.html')

@login_required(login_url='login')
def solo_output(req):
    return render(req, 'solo_output.html')