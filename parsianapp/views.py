from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results,submit_company,disease,order
from .forms import registration, summary_of_results_form,submit_company_form,disease_form,order_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.views import generic
from . import forms, models
from django.core.paginator import Paginator


def home_view(request):
    return render(request, 'home.html')


def contact_us_view(request):
    return render(request, 'contact_us.html')


def occupational_medicine_view(request):
    return render(request, 'occupational_medicine.html')


def services_view(request):
    return render(request, 'services.html')


def register_view(request):
    form = registration()
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account made succcessfuly for ' + user)
            return redirect('../login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('../manage')
        else:
            messages.info(request, 'username or password is incorect')
    return render(request, 'login.html')


@login_required(login_url='login')
def manage_view(request):
    return render(request, 'manage.html')


@login_required(login_url='login')
def submit_person_view(request):
    work=summary_of_results.objects.last()
    code_list=submit_company.objects.order_by('id')
    if work:
        code=work.examinations_code
    else:
        code=''
    initial_dict = {
        'examinations_code':code
        
    }
    messages.error(request,'خارج از بازه تعریف شده')
    form=summary_of_results_form(initial=initial_dict)
    context={'form':form,
    'code_list':code_list}
    return render(request,'summary_of_results.html',context)


@require_POST
def addperson_view(request):
    form = summary_of_results_form(request.POST)
    if form.is_valid():
        new_summary = form.save()
    return redirect('submit_person')


def logoutuser_view(request):
    logout(request)
    return redirect('../')


@login_required(login_url='login')
def company_view(request):
    form=submit_company_form()
    context={'form':form}
    return render(request, 'submit_company.html',context)


@require_POST
def addcompany_view(request):
    form=submit_company_form(request.POST)
    if form.is_valid():
        new_company=form.save()
    return redirect('submit_company')

@login_required(login_url='login')
def output_view(request):
    form=disease_form()
    code_list=submit_company.objects.order_by('id')
    context={'form':form,'code_list':code_list}
    return render(request,'output.html',context)

@require_POST
def adddisease_view(request):
    form=disease_form(request.POST)
    if form.is_valid():
        new_disease=form.save()
    return redirect('output')


@login_required(login_url='login')
def disease_code_view(request):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company}
    return render(request, 'disease_code.html',context)

@login_required(login_url='login')
def open_docs_view(request):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company}
    return render(request, 'open_docs.html',context)

@login_required(login_url='login')
def summary_of_examinations_view(request):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company}
    return render(request, 'summary_of_examinations.html',context)

@login_required(login_url='login')
def problem_view(request):
    work=disease.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=summary_of_results.objects.filter(examinations_code=code)
    company=submit_company.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company}
    return render(request, 'problem.html',context)

@login_required(login_url='login')
def specialist_view(request):
    return render(request, 'specialist.html')

@login_required(login_url='login')
def graph_view(request):
    return render(request, 'graph.html')

@login_required(login_url='login')
def solo_output_view(request):
    work=disease.objects.last()
    model=order.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    if model:
        number=model.order_number
    else:
        number='1'
    Summary=summary_of_results.objects.filter(examinations_code=code)
    p = Paginator(summary_of_results.objects.filter(examinations_code=code),number)
    page=request.GET.get('page')
    solo_page=p.get_page(page)
    company=submit_company.objects.filter(examinations_code=code)
    nums='a' * solo_page.paginator.num_pages
    initial_dict = {
        'order_number':number
        
    }
    form=order_form(initial=initial_dict)
    context={'Summary':Summary,'Company':company,'solo_page':solo_page,'nums':nums,'form':form}
    return render(request, 'solo_output.html',context)

@login_required(login_url='login')
def input_view(request):
    return render(request, 'input.html')

@require_POST
def addorder_view(request):
    form=order_form(request.POST)
    if form.is_valid():
        new_order=form.save()
    return redirect('solo_output')    