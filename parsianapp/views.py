from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Summary_Of_Results_Model,Submit_Company_Model,Disease_Model,Personal_Species_Model,Job_History_Model,Assessment_Model,Personal_History_Model,Examinations_Model,Experiments_Model,Para_Clinic_Model,Consulting_Model,Final_Theory_Model,Summary_Of_Results
from .forms import registration, summary_of_results_form,submit_company_form,disease_form,personal_species_form,job_history_form,assessment_form,personal_history_form,examinations_form,experiments_form,para_clinic_form,consulting_form,final_theory_form,submit_course_form
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
    work=Summary_Of_Results_Model.objects.last()
    code_list=Submit_Company_Model.objects.order_by('id')
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
    return render(request,'examinations.html',context)


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
def submit_course_view(request):
    form=submit_course_form()
    context={'form':form}
    return render(request, 'submit_course.html',context)


@require_POST
def addcourse_view(request):
    form=submit_course_form(request.POST)
    if form.is_valid():
        new_company=form.save()
    return redirect('submit_course')


@login_required(login_url='login')
def submit_company_view(request):
    form=submit_company_form()
    context={'form':form}
    return render(request, 'submit_company.html',context)


@require_POST
def addcompany_view(request):
    form=submit_company_form(request.POST)
    if form.is_valid():
        new_company=form.save()
    return redirect('submit_ccompany')

@login_required(login_url='login')
def output_view(request):
    form=disease_form()
    code_list=Submit_Company_Model.objects.order_by('id')
    context={'form':form,'code_list':code_list}
    return render(request,'output.html',context)

@require_POST
def adddisease_view(request):
    model=Disease_Model.objects.get(pk=1)
    form=disease_form(request.POST)
    if form.is_valid():
        model.examinations_code=form.cleaned_data['examinations_code']
        model.save()
    return redirect('output')


@login_required(login_url='login')
def disease_code_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    summary_of_results=Summary_Of_Results.objects.all()
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    context={'Summary':summary_of_results,'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory}
    return render(request, 'disease_code.html',context)

@login_required(login_url='login')
def open_docs_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory}
    return render(request, 'open_docs.html',context)

@login_required(login_url='login')
def summary_of_examinations_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory}
    return render(request, 'summary_of_examinations.html',context)

@login_required(login_url='login')
def problem_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    context={'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory}
    return render(request, 'problem.html',context)

@login_required(login_url='login')
def specialist_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    return render(request, 'specialist.html')

@login_required(login_url='login')
def graph_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    count=0
    a_tri,b_tri,c_tri=0,0,0
    data_tri=[]
    a_chl,b_chl,c_chl=0,0,0
    data_chl=[]
    a_sug,b_sug,c_sug,d_sug=0,0,0,0
    data_sug=[]
    a_pre,b_pre,c_pre,d_pre=0,0,0,0
    data_pre=[]
    a_ry,b_ry,c_ry=0,0,0
    data_ry=[]
    a_ly,b_ly,c_ly=0,0,0
    data_ly=[]
    a_esp,b_esp,c_esp,d_esp,e_esp,f_esp=0,0,0,0,0,0
    data_esp=[]
    a_rg,b_rg,c_rg,d_rg,e_rg,f_rg=0,0,0,0,0,0
    data_rg=[]
    a_lg,b_lg,c_lg,d_lg,e_lg,f_lg=0,0,0,0,0,0
    data_lg=[]
    a_u,b_u,c_u=0,0,0
    data_u=[]
    a_p,b_p,c_p,d_p,e_p=0,0,0,0,0
    data_p=[]
    a_s,b_s,c_s,d_s=0,0,0,0
    data_s=[]
    a_psa,b_psa,c_psa=0,0,0
    data_psa=[]
    a_n,b_n,c_n,d_n,e_n=0,0,0,0,0
    data_n=[]
    a_d,b_d,c_d,d_d,e_d=0,0,0,0,0
    data_d=[]
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    for summary in Summary:
        count+=1
        if summary.triglyceride < 200:
            a_tri += 1
        elif summary.triglyceride >= 200:
            b_tri += 1
        else:
            c_tri += 1    
    data_tri.append(a_tri)
    data_tri.append(b_tri)
    data_tri.append(c_tri)


    for summary in Summary:
        if summary.cholesterol < 200:
            a_chl += 1
        elif summary.cholesterol >= 200:
            b_chl += 1
        else:
            c_chl += 1    
    data_chl.append(a_chl)
    data_chl.append(b_chl)
    data_chl.append(c_chl)


    for summary in Summary:
        if summary.blood_sugar < 100:
            a_sug += 1
        elif summary.blood_sugar < 126:
            b_sug += 1
        elif summary.blood_sugar >=126:
            c_sug += 1
        else:
            d_sug += 1    
    data_sug.append(a_sug)
    data_sug.append(b_sug)
    data_sug.append(c_sug)
    data_sug.append(d_sug)

    for summary in Summary:
        if summary.blood_pressure < 9:
            c_pre += 1
        elif summary.blood_pressure >= 9 and summary.blood_pressure <= 14:
            a_pre += 1
        elif summary.blood_pressure > 14:
            b_pre += 1
        else:
            d_pre += 1
    data_pre.append(a_pre)
    data_pre.append(b_pre)
    data_pre.append(c_pre)
    data_pre.append(d_pre)  



    for summary in Summary:
        if summary.right_eye_vision < 1:
            b_ry += 1
        elif summary.right_eye_vision >= 1:
            a_ry += 1
        else:
            c_ry += 1    
    data_ry.append(a_ry)
    data_ry.append(b_ry)
    data_ry.append(c_ry)


    for summary in Summary:
        if summary.left_eye_vision < 1:
            b_ly += 1
        elif summary.left_eye_vision >= 1:
            a_ly += 1
        else:
            c_ly += 1    
    data_ly.append(a_ly)
    data_ly.append(b_ly)
    data_ly.append(c_ly)


    for summary in Summary:
        if summary.breathing_test == 'normal':
            a_esp += 1
        elif summary.breathing_test == 'tahdidi':
            b_esp += 1
        elif summary.breathing_test == 'ensedadi':
            c_esp += 1
        elif summary.breathing_test == 'try':
            d_esp += 1
        elif summary.breathing_test == 'namaie_toaman':
            e_esp += 1
        elif summary.breathing_test == 'none' or summary.breathing_test == 'null':
            f_esp += 1
    data_esp.append(a_esp)
    data_esp.append(b_esp)
    data_esp.append(c_esp)
    data_esp.append(d_esp) 
    data_esp.append(e_esp)
    data_esp.append(f_esp) 

    for summary in Summary:
        if summary.right_ear_hearing == 'normal':
            a_rg += 1
        elif summary.right_ear_hearing == 'kahesh_shenavai_hedayati':
            b_rg += 1
        elif summary.right_ear_hearing == 'kahesh_shenavai_hesi_asabi':
            c_rg += 1
        elif summary.right_ear_hearing == 'kahesh_shenavai_nashi_az_seda':
            d_rg += 1
        elif summary.right_ear_hearing == 'toaman_hedayati_va_hesi_asabi':
            e_rg += 1
        elif summary.right_ear_hearing == 'none' or summary.right_ear_hearing == 'null':
            f_rg += 1
    data_rg.append(a_rg)
    data_rg.append(b_rg)
    data_rg.append(c_rg)
    data_rg.append(d_rg) 
    data_rg.append(e_rg)
    data_rg.append(f_rg) 



    for summary in Summary:
        if summary.left_ear_hearing == 'normal':
            a_lg += 1
        elif summary.left_ear_hearing == 'kahesh_shenavai_hedayati':
            b_lg += 1
        elif summary.left_ear_hearing == 'kahesh_shenavai_hesi_asabi':
            c_lg += 1
        elif summary.left_ear_hearing == 'kahesh_shenavai_nashi_az_seda':
            d_lg += 1
        elif summary.left_ear_hearing == 'toaman_hedayati_va_hesi_asabi':
            e_lg += 1
        elif summary.left_ear_hearing == 'none' or summary.left_ear_hearing == 'null':
            f_lg += 1
    data_lg.append(a_lg)
    data_lg.append(b_lg)
    data_lg.append(c_lg)
    data_lg.append(d_lg) 
    data_lg.append(e_lg)
    data_lg.append(f_lg)


    for summary in Summary:
        if summary.urine == 'normal':
            a_u += 1
        elif summary.urine == 'not_normal':
            b_u += 1
        elif summary.urine == 'none' or summary.urine == 'null':
            c_u += 1  
    data_u.append(a_u)
    data_u.append(b_u)
    data_u.append(c_u) 



    for summary in Summary:
        if summary.final_theory == 'belamane':
            a_p += 1
        elif summary.final_theory == 'taghir_shekl':
            b_p += 1
        elif summary.final_theory == 'mashrot':
            c_p += 1
        elif summary.final_theory == 'comision':
            d_p += 1
        elif  summary.final_theory == 'null':
            e_p += 1
    data_p.append(a_p)
    data_p.append(b_p)
    data_p.append(c_p)
    data_p.append(d_p)
    data_p.append(e_p)

    for summary in Summary:
        if summary.blood_lead < 20:
            a_s += 1
        elif summary.blood_lead < 30:
            b_s += 1
        elif summary.blood_lead >=30:
            c_s += 1
        else:
            d_s += 1    
    data_s.append(a_s)
    data_s.append(b_s)
    data_s.append(c_s)
    data_s.append(d_s)



    for summary in Summary:
        if summary.PSA < 4:
            a_psa += 1
        elif summary.PSA >= 4:
            b_psa += 1
        else:
            c_psa += 1    
    data_psa.append(a_psa)
    data_psa.append(b_psa)
    data_psa.append(c_psa)


    for summary in Summary:
        if summary.heart == 'normal':
            a_n += 1
        elif summary.heart == 'taghirat_gheir_ekhtesasi':
            b_n += 1
        elif summary.heart == 'try':
            c_n += 1
        elif summary.heart == 'not_normal':
            d_n += 1
        elif  summary.heart == 'null' or summary.heart == 'none'  :
            e_n += 1
    data_n.append(a_n)
    data_n.append(b_n)
    data_n.append(c_n)
    data_n.append(d_n)
    data_n.append(e_n)


    for summary in Summary:
        if summary.D3 < 10:
            a_d += 1
        elif summary.D3 < 30:
            b_d += 1
        elif summary.D3 < 101:
            c_d += 1
        elif summary.D3 >= 101:
            d_d += 1
        else: 
            e_d += 1
    data_d.append(a_d)
    data_d.append(b_d)
    data_d.append(c_d)
    data_d.append(d_d)
    data_d.append(e_d)



    data=[data_tri,
    data_chl,
    data_sug,
    data_pre,
    data_ry,
    data_ly,
    data_esp,
    data_rg,
    data_lg,
    data_u,
    data_p,
    data_s,
    data_psa,
    data_n,
    data_d]
    context={'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'data':data,'count':count}
    return render(request, 'graph.html',context)

@login_required(login_url='login')
def solo_output_view(request):
    personal_species=Personal_Species_Model.objects.all()
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    work=Disease_Model.objects.last()
    model=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    if model:
        number=model.order_number
    else:
        number='1'
    Summary=Summary_Of_Results_Model.objects.filter(examinations_code=code)
    p = Paginator(Summary_Of_Results_Model.objects.filter(examinations_code=code),number)
    page=request.GET.get('page')
    solo_page=p.get_page(page)
    company=Submit_Company_Model.objects.filter(examinations_code=code)
    nums='a' * solo_page.paginator.num_pages
    initial_dict = {
        'order_number':number
        
    }
    form=disease_form(initial=initial_dict)
    context={'Summary':Summary,'Company':company,'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'solo_page':solo_page,'nums':nums,'form':form}
    return render(request, 'solo_output.html',context)

@login_required(login_url='login')
def input_view(request):
    return render(request, 'input.html')

@require_POST
def addorder_view(request):
    model=Disease_Model.objects.get(pk=1)
    form=disease_form(request.POST)
    if form.is_valid():
        model.order_number=form.cleaned_data['order_number']
        model.save()
    return redirect('solo_output')    


@login_required(login_url='login')
def examinations_view(request):
    personal_species=personal_species_form()
    job_history=job_history_form()
    assessment=assessment_form()
    personal_history=personal_history_form()
    examinations=examinations_form()
    experiments=experiments_form()
    para_clinic=para_clinic_form()
    consulting=consulting_form()
    final_theory=final_theory_form()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory }
    return render(request, 'examinations.html',context)

@require_POST
def addexaminations_view(request):
    personal_species=personal_species_form(request.POST)
    job_history=job_history_form(request.POST)
    assessment=assessment_form(request.POST)
    personal_history=personal_history_form(request.POST)
    examinations=examinations_form(request.POST)
    experiments=experiments_form(request.POST)
    para_clinic=para_clinic_form(request.POST)
    consulting=consulting_form(request.POST)
    final_theory=final_theory_form(request.POST)
    if personal_species.is_valid():
        personal_species.save()
    if job_history.is_valid():
        job_history.save()
    if assessment.is_valid():
        assessment.save()
    if personal_history.is_valid():
        personal_history.save()
    if examinations.is_valid():
        examinations.save()
    if experiments.is_valid():
        experiments.save()
    if para_clinic.is_valid():
        para_clinic.save()
    if consulting.is_valid():
        consulting.save()
    if final_theory.is_valid():
        final_theory.save()
    return redirect('examinations')


@login_required(login_url='login')
def examinations_output_view(request):
    personal_species=Personal_Species_Model.objects.get(pk=1)
    job_history=Job_History_Model.objects.get(pk=1)
    assessment=Assessment_Model.objects.get(pk=1)
    personal_history=Personal_History_Model.objects.get(pk=1)
    examinations=Examinations_Model.objects.get(pk=1)
    experiments=Experiments_Model.objects.get(pk=1)
    para_clinic=Para_Clinic_Model.objects.get(pk=1)
    consulting=Consulting_Model.objects.get(pk=1)
    final_theory=Final_Theory_Model.objects.get(pk=1)
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory }
    return render(request, 'examinations_output.html',context)
