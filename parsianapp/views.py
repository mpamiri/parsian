from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse , Http404
from django.contrib.auth.forms import UserCreationForm
from .models import Disease_Model,Personal_Species_Model,Job_History_Model,Assessment_Model,Personal_History_Model,Examinations_Model,Experiments_Model,Para_Clinic_Model,Consulting_Model,Final_Theory_Model,ExaminationsCourse
from .forms import registration,disease_form,personal_species_form,job_history_form,assessment_form,personal_history_form,examinations_form,experiments_form,para_clinic_form,consulting_form,final_theory_form,submit_course_form
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST
from django.views import generic
from . import forms, models
from django.core.paginator import Paginator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import move
import os
from fpdf import FPDF
import pyautogui
from time import sleep
from PIL import Image



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
            return redirect('../')
        else:
            messages.info(request, 'username or password is incorect')
    return render(request, 'login.html')




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
    return redirect('submit_company')

@login_required(login_url='login')
def output_view(request):
    form=disease_form()
    code_list=ExaminationsCourse.objects.order_by('id')
    context={'form':form,'code_list':code_list}
    return render(request,'output.html',context)

@require_POST
def adddisease_view(request):
    if Disease_Model:
        model=Disease_Model.objects.last()
    else:
        a = Disease_Model(examinations_code='',order_number=1)
        a.save()
        model=Disease_Model.objects.last()
    form=disease_form(request.POST)
    if form.is_valid():
        model.examinations_code=form.cleaned_data['examinations_code']
        model.save()
    return redirect('output')


@login_required(login_url='login')
def disease_code_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory, 'examinations_course':examinations_course}
    return render(request, 'disease_code.html',context)


def disease_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('bot')
    password.send_keys('botamiri84')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/disease_code")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1920,S('Height'))
    count = 0
    i = 0
    pdf = FPDF()
    while i <= count :
        driver.find_element('id','disease' + str(i)).screenshot('images/'+ str(i) +'disease_img.png')
        driver.find_element('id','Head').screenshot('images/Head_img.png')
        pdf.add_page()
        pdf.image('images/Head_img.png',-1,None,220,22)
        pdf.image('images/'+ str(i) +'disease_img.png',3,None,200,200)
        os.remove('images/'+ str(i) +'disease_img.png')
        os.remove('images/Head_img.png')
        i += 1
    pdf.output("pdfs/disease.pdf", "F")
    file_path = os.path.join('pdfs/disease.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url='login')
def open_docs_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course,final__mashrot='False',final__belamane='False',final__rad='False')
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory , 'examinations_course':examinations_course}
    return render(request, 'open_docs.html',context)


def open_docs_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course,final__mashrot='False',final__belamane='False',final__rad='False')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/open_docs")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1920,S('Height'))
    count = 0
    i = 1
    pdf = FPDF()
    pdf.add_page()
    driver.find_element('id','Head').screenshot('images/Head_img.png')
    driver.find_element('id','open0').screenshot('images/open0_img.png')
    pdf.image('images/Head_img.png',-1,None,220,22)
    pdf.image('images/open0_img.png',3,None,200,10)
    os.remove('images/Head_img.png')
    os.remove('images/open0_img.png')
    for x in personal_species:
        count += 1
    while i <= count:
        if (i - 1) % 20 == 0 and i != 1:
            driver.find_element('id','open' + str(i)).screenshot('images/'+ str(i) +'open_img.png')
            driver.find_element('id','Head').screenshot('images/Head_img.png')
            driver.find_element('id','open0').screenshot('images/open0_img.png')
            pdf.add_page()
            pdf.image('images/Head_img.png',-1,None,220,22)
            pdf.image('images/open0_img.png',3,None,200,10)
            pdf.image('images/'+ str(i) +'open_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'open_img.png')
            os.remove('images/open0_img.png')
            os.remove('images/Head_img.png')
            i += 1 
        else:   
            driver.find_element('id','open' + str(i)).screenshot('images/'+ str(i) +'open_img.png')
            pdf.image('images/'+ str(i) +'open_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'open_img.png')
            i += 1
    pdf.output("pdfs/open.pdf", "F")
    file_path = os.path.join('pdfs/open.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url='login')
def summary_of_examinations_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory , 'examinations_course':examinations_course}
    return render(request, 'summary_of_examinations.html',context)



def summary_of_examinations_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/summary_of_examinations")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1920,S('Height'))
    count = 0
    i = 1
    pdf = FPDF()
    pdf.add_page()
    driver.find_element('id','Head').screenshot('images/Head_img.png')
    driver.find_element('id','summary0').screenshot('images/summary0_img.png')
    pdf.image('images/Head_img.png',-1,None,220,22)
    pdf.image('images/summary0_img.png',3,None,200,22)
    os.remove('images/Head_img.png')
    os.remove('images/summary0_img.png')
    for x in personal_species:
        count += 1
    while i <= count: 
        if (i - 1) % 15 == 0 and i != 1:
            driver.find_element('id','summary' + str(i)).screenshot('images/'+ str(i) +'summary_img.png')
            driver.find_element('id','Head').screenshot('images/Head_img.png')
            driver.find_element('id','summary0').screenshot('images/summary0_img.png')
            pdf.add_page()
            pdf.image('images/Head_img.png',-1,None,220,22)
            pdf.image('images/summary0_img.png',3,None,200,20)
            pdf.image('images/'+ str(i) +'summary_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'summary_img.png')
            os.remove('images/summary0_img.png')
            os.remove('images/Head_img.png')
            i += 1 
        else:   
            driver.find_element('id','summary' + str(i)).screenshot('images/'+ str(i) +'summary_img.png')
            pdf.image('images/'+ str(i) +'summary_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'summary_img.png')
            i += 1
    pdf.output("pdfs/summary.pdf", "F")
    file_path = os.path.join('pdfs/summary.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url='login')
def problem_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'examinations_course':examinations_course}
    return render(request, 'problem.html',context)
def problem_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/problem")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    count = 0
    i = 1
    pdf = FPDF()
    pdf.add_page()
    driver.find_element('id','Head').screenshot('images/Head_img.png')
    driver.find_element('id','problem0').screenshot('images/problem0_img.png')
    pdf.image('images/Head_img.png',-1,None,220,22)
    pdf.image('images/problem0_img.png',3,None,200,22)
    os.remove('images/Head_img.png')
    os.remove('images/problem0_img.png')
    for x in personal_species:
        count += 1
    while i <= count: 
        if (i - 1) % 15 == 0 and i != 1:
            driver.find_element('id','problem' + str(i)).screenshot('images/'+ str(i) +'problem_img.png')
            driver.find_element('id','Head').screenshot('images/Head_img.png')
            driver.find_element('id','problem0').screenshot('images/problem0_img.png')
            pdf.add_page()
            pdf.image('images/Head_img.png',-1,None,220,22)
            pdf.image('images/problem0_img.png',3,None,200,20)
            pdf.image('images/'+ str(i) +'problem_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'problem_img.png')
            os.remove('images/problem0_img.png')
            os.remove('images/Head_img.png')
            i += 1 
        else:   
            driver.find_element('id','problem' + str(i)).screenshot('images/'+ str(i) +'problem_img.png')
            pdf.image('images/'+ str(i) +'problem_img.png',3,None,200,10)
            os.remove('images/'+ str(i) +'problem_img.png')
            i += 1
    pdf.output("pdfs/problem.pdf", "F")
    file_path = os.path.join('pdfs/problem.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
@login_required(login_url='login')
def specialist_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'examinations_course':examinations_course}
    return render(request, 'specialist.html',context)

@login_required(login_url='login')
def graph_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
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
    a_p,b_p,c_p,e_p=0,0,0,0,
    data_p=[]
    a_s,b_s,c_s,d_s=0,0,0,0
    data_s=[]
    a_psa,b_psa,c_psa=0,0,0
    data_psa=[]
    a_n,b_n,c_n,d_n,e_n=0,0,0,0,0
    data_n=[]
    a_d,b_d,c_d,d_d,e_d=0,0,0,0,0
    data_d=[]
    count=0
    for summary in personal_species:
        count+=1
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.tg:
            c_tri += 1
        elif experiments.tg_status == False:
            b_tri += 1
        else:
            a_tri += 1    
    data_tri.append(a_tri)
    data_tri.append(b_tri)
    data_tri.append(c_tri)


    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.chol:
            c_chl += 1
        elif experiments.chol_status == False:
            b_chl += 1
        else:
            a_chl += 1   
    data_chl.append(a_chl)
    data_chl.append(b_chl)
    data_chl.append(c_chl)


    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.fbs ==  None:
            d_sug += 1   
        elif experiments.fbs < 100:
            a_sug += 1
        elif experiments.fbs < 126:
            b_sug += 1
        elif experiments.fbs >=126:
            c_sug += 1  
    data_sug.append(a_sug)
    data_sug.append(b_sug)
    data_sug.append(c_sug)
    data_sug.append(d_sug)

    for summary in personal_species:
        examinations=Examinations_Model.objects.filter(person=summary).last()
        if examinations.blood_pressure == None:
            d_pre += 1
        elif examinations.blood_pressure < 9:
            c_pre += 1
        elif examinations.blood_pressure >= 9 and examinations.blood_pressure <= 14:
            a_pre += 1
        elif examinations.blood_pressure > 14:
            b_pre += 1
    data_pre.append(a_pre)
    data_pre.append(b_pre)
    data_pre.append(c_pre)
    data_pre.append(d_pre)  



    for summary in personal_species:
        para=Para_Clinic_Model.objects.filter(person=summary).last()
        if para.opto_hedat_r_bi == None:
            c_ry += 1 
        elif para.opto_hedat_r_bi < 10:
            b_ry += 1
        elif summary.opto_hedat_r_bi == 10:
            a_ry += 1   
    data_ry.append(a_ry)
    data_ry.append(b_ry)
    data_ry.append(c_ry)


    for summary in personal_species:
        para=Para_Clinic_Model.objects.filter(person=summary).last()
        if para.opto_hedat_l_bi == None:
            c_ly += 1 
        elif para.opto_hedat_l_bi < 10:
            b_ly += 1
        elif summary.opto_hedat_l_bi == 10:
            a_ly += 1  
    data_ly.append(a_ly)
    data_ly.append(b_ly)
    data_ly.append(c_ly)


    for summary in personal_species:
        para=Para_Clinic_Model.objects.filter(person=summary).last()
        if para.espiro_tafsir == 'normal':
            a_esp += 1
        elif para.espiro_tafsir == 'tahdidi':
            b_esp += 1
        elif para.espiro_tafsir == 'ensedadi':
            c_esp += 1
        elif para.espiro_tafsir == 'try':
            d_esp += 1
        elif para.espiro_tafsir == 'namaie_toaman':
            e_esp += 1
        elif para.espiro_tafsir == None:
            f_esp += 1
    data_esp.append(a_esp)
    data_esp.append(b_esp)
    data_esp.append(c_esp)
    data_esp.append(d_esp) 
    data_esp.append(e_esp)
    data_esp.append(f_esp) 

    for summary in personal_species:
        para=Para_Clinic_Model.objects.filter(person=summary).last()
        if para.audio_r_tafsir == 'normal':
            a_rg += 1
        elif para.audio_r_tafsir == 'kahesh_shenavai_hedayati':
            b_rg += 1
        elif para.audio_r_tafsir == 'kahesh_shenavai_hesi_asabi':
            c_rg += 1
        elif para.audio_r_tafsir == 'kahesh_shenavai_nashi_az_seda':
            d_rg += 1
        elif para.audio_r_tafsir == 'toaman_hedayati_va_hesi_asabi':
            e_rg += 1
        elif para.audio_r_tafsir == None:
            f_rg += 1
    data_rg.append(a_rg)
    data_rg.append(b_rg)
    data_rg.append(c_rg)
    data_rg.append(d_rg) 
    data_rg.append(e_rg)
    data_rg.append(f_rg) 



    for summary in personal_species:
        para=Para_Clinic_Model.objects.filter(person=summary).last()
        if para.audio_l_tafsir == 'normal':
            a_lg += 1
        elif para.audio_l_tafsir == 'kahesh_shenavai_hedayati':
            b_lg += 1
        elif para.audio_l_tafsir == 'kahesh_shenavai_hesi_asabi':
            c_lg += 1
        elif para.audio_l_tafsir == 'kahesh_shenavai_nashi_az_seda':
            d_lg += 1
        elif para.audio_l_tafsir == 'toaman_hedayati_va_hesi_asabi':
            e_lg += 1
        elif para.audio_l_tafsir == None:
            f_lg += 1
    data_lg.append(a_lg)
    data_lg.append(b_lg)
    data_lg.append(c_lg)
    data_lg.append(d_lg) 
    data_lg.append(e_lg)
    data_lg.append(f_lg) 


    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.ua_prot == None or experiments.ua_glu == None or experiments.ua_rbc == None or experiments.ua_wbc == None or experiments.ua_bact == None:
            c_u += 1
        elif experiments.ua_prot_status == False or experiments.ua_glu_status == False or experiments.ua_rbc_status == False or experiments.ua_wbc_status == False or experiments.ua_bact_status == False:
            b_u += 1
        else:
            a_u += 1  
    data_u.append(a_u)
    data_u.append(b_u)
    data_u.append(c_u) 



    for summary in personal_species:
        final=Final_Theory_Model.objects.filter(person=summary).last()
        if final.belamane == True:
            a_p += 1
        elif final.rad == True:
            b_p += 1
        elif final.mashrot == True:
            c_p += 1
        else:
            e_p += 1
    data_p.append(a_p)
    data_p.append(b_p)
    data_p.append(c_p)
    data_p.append(e_p)

    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.lead == None:
            d_s += 1  
        elif experiments.lead < 20:
            a_s += 1
        elif experiments.lead < 30:
            b_s += 1
        elif experiments.lead >=30:
            c_s += 1  
    data_s.append(a_s)
    data_s.append(b_s)
    data_s.append(c_s)
    data_s.append(d_s)



    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.psa == None:
            c_psa += 1  
        elif experiments.psa_status == True:
            a_psa += 1
        elif experiments.psa_status == False:
            b_psa += 1  
    data_psa.append(a_psa)
    data_psa.append(b_psa)
    data_psa.append(c_psa)


    for summary in personal_species:
        para = Para_Clinic_Model.objects.filter(person=summary).last()
        if para.other_ecg == 'normal':
            a_n += 1
        elif para.other_ecg == 'not_ekhtesasi':
            b_n += 1
        elif para.other_ecg == 'again':
            c_n += 1
        elif para.other_ecg == 'not_normal':
            d_n += 1
        elif  para.other_ecg == None :
            e_n += 1
    data_n.append(a_n)
    data_n.append(b_n)
    data_n.append(c_n)
    data_n.append(d_n)
    data_n.append(e_n)


    for summary in personal_species:
        experiments=Experiments_Model.objects.filter(person=summary).last()
        if experiments.d == None: 
            e_d += 1
        elif experiments.d < 10:
            a_d += 1
        elif experiments.d < 30:
            b_d += 1
        elif experiments.d < 101:
            c_d += 1
        elif experiments.d >= 101:
            d_d += 1
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
    context={'personal_species' : personal_species ,'examinations_course':examinations_course,'data':data,'count':count}
    return render(request, 'graph.html',context)


def graph_pdf_view(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/graph")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1920,S('Height'))
    pdf = FPDF()
    driver.find_element('id','Head').screenshot('images/Head_img.png')
    pdf.add_page()
    pdf.image('images/Head_img.png',-1,None,220,22)
    os.remove('images/Head_img.png')
    pdf.line(0, 31.5, 220, 31.5)
    i = 0
    while i <= 14:        
        if i % 2 == 0 and i != 0:
            driver.find_element('id','graph' + str(i)).screenshot('images/'+ str(i) +'graph_img.png')
            pdf.add_page()
            pdf.image('images/'+ str(i) +'graph_img.png',10,None,200,100)
            os.remove('images/'+ str(i) +'graph_img.png')
            i += 1 
        else:
            driver.find_element('id','graph' + str(i)).screenshot('images/'+ str(i) +'graph_img.png')
            pdf.image('images/'+ str(i) +'graph_img.png',10,None,200,100)
            os.remove('images/'+ str(i) +'graph_img.png')
            i += 1 
    pdf.output("pdfs/graph.pdf", "F")
    file_path = os.path.join('pdfs/graph.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

@login_required(login_url='login')
def solo_output_view(request):
    solo_output_view.current_path = request.get_full_path()
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    job_history=Job_History_Model.objects.all()
    assessment=Assessment_Model.objects.all()
    personal_history=Personal_History_Model.objects.all()
    examinations=Examinations_Model.objects.all()
    experiments=Experiments_Model.objects.all()
    para_clinic=Para_Clinic_Model.objects.all()
    consulting=Consulting_Model.objects.all()
    final_theory=Final_Theory_Model.objects.all()
    count = 0
    for x in personal_species:
        count += 1
    if count % work.order_number == 0:
        count = count // work.order_number
    else:
        count = (count // work.order_number) + 1
    if work:
        number=work.order_number
    else:
        number='1'
    p = Paginator(Personal_Species_Model.objects.filter(examinations_code=examinations_course),number)
    page=request.GET.get('page')
    solo_page=p.get_page(page)
    nums='a' * solo_page.paginator.num_pages
    initial_dict = {
        'order_number':number       
    }
    form=disease_form(initial=initial_dict)
    context={'personal_species' : personal_species,'form' :form,'examinations_course' : examinations_course,'solo_page':solo_page,'nums':nums,'count': count }
    return render(request, 'solo_output.html',context)

def solo_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000"+solo_output_view.current_path)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    i = 0
    count = 0
    pdf = FPDF('P', 'mm', 'A5')
    for x in personal_species:
        count += 1
    n = count
    if count < work.order_number:
        last_count = count
    elif count % work.order_number == 0:
        count = count // work.order_number
        last_count = 0
    else:
        count = (count // work.order_number) + 1
        last_count = n - ((count - 1) * work.order_number)
    if n < work.order_number:
        while i < last_count :
            i += 1    
            driver.find_element('id','print' + str(i)).screenshot('images/'+ str(i) +'solo_img.png')
            pdf.add_page()
            pdf.image('images/'+ str(i) +'solo_img.png',0,None,140,140)
            os.remove('images/'+ str(i) +'solo_img.png')
        pdf.output("pdfs/solo.pdf", "F")
        driver.quit()
    elif solo_output_view.current_path == ('/output/solo_output?page=' + str(count)):
        while i < last_count :
            i += 1    
            driver.find_element('id','print' + str(i)).screenshot('images/'+ str(i) +'solo_img.png')
            pdf.add_page()
            pdf.image('images/'+ str(i) +'solo_img.png',0,None,140,140)
            os.remove('images/'+ str(i) +'solo_img.png')
        pdf.output("pdfs/solo.pdf", "F")
        driver.quit()
    else:
        while i < work.order_number :
            i += 1    
            driver.find_element('id','print' + str(i)).screenshot('images/'+ str(i) +'solo_img.png')
            pdf.add_page()
            pdf.image('images/'+ str(i) +'solo_img.png',0,None,140,140)
            os.remove('images/'+ str(i) +'solo_img.png')
        pdf.output("pdfs/solo.pdf", "F")
        driver.quit()
    file_path = os.path.join('pdfs/solo.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

@login_required(login_url='login')
def input_view(request):
    return render(request, 'input.html')

@require_POST
def addorder_view(request):
    model=Disease_Model.objects.last()
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
    e_items=''
    items = ''
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
        new_person = personal_species.save()
    if personal_species.is_valid() and  job_history.is_valid():
        new_job_history = job_history.save(commit=False)
        new_job_history.person = new_person
        new_job_history.durations = ((new_job_history.current_job_to_year * 12) + new_job_history.current_job_to_month) - ((new_job_history.current_job_from_year * 12) + new_job_history.current_job_from_month)
        new_job_history.save()
    if personal_species.is_valid() and  assessment.is_valid():
        new_assessment = assessment.save(commit=False)
        new_assessment.person = new_person
        if new_assessment.current_ph_noise == True:
            items += ' ???? ?? ??????/'
        if new_assessment.current_ph_erteash == True:
            items += ' ????????????/'
        if new_assessment.current_ph_not_unizan == True:
            items += ' ???????? ?????? ??????????????/'
        if new_assessment.current_ph_unizan == True:
            items += ' ???????? ??????????????/'
        if new_assessment.current_ph_stress == True:
            items += ' ?????????? ????????????/'
        if new_assessment.current_sh_dust == True:
            items += ' ?????? ?? ????????/'
        if new_assessment.current_sh_metals == True:
            items += ' ?????? ??????????/'
        if new_assessment.current_sh_halal == True:
            items += ' ????????/'
        if new_assessment.current_sh_afat == True:
            items += ' ?????? ????????/'
        if new_assessment.current_sh_asidvbaz == True:
            items += ' ???????? ?? ??????????/'
        if new_assessment.current_sh_gaz == True:
            items += ' ?????? ????/'
        if new_assessment.current_bio_gazesh == True:
            items += ' ??????/'
        if new_assessment.current_bio_bactery == True:
            items += ' ????????????/'
        if new_assessment.current_bio_virus == True:
            items += ' ??????????/'
        if new_assessment.current_bio_angal == True:
            items += ' ????????/'
        if new_assessment.current_er_standvsit == True:
            items += ' ?????????????? ???? ?????????? ???????????? ??????/'
        if new_assessment.current_er_loop == True:
            items += ' ?????? ????????????/'
        if new_assessment.current_er_hamlvnaghl == True:
            items += ' ?????? ?? ?????? ?????? ??????????/'
        if new_assessment.current_er_vaziat_namonaseb == True:
            items += ' ?????????? ?????????????? ??????/'
        if new_assessment.current_rav_order == True:
            items += ' ???????? ????????/'
        if new_assessment.current_rav_stressor == True:
            items += ' ?????????????? ?????? ????????/'  
        if new_assessment.required_description:
            items += new_assessment.required_description
        new_assessment.assessments = items    
        new_assessment.save()
    if personal_species.is_valid() and  personal_history.is_valid():
        new_personal_history = personal_history.save(commit=False)
        new_personal_history.person = new_person
        new_personal_history.save()
    if personal_species.is_valid() and  examinations.is_valid():
        new_examinations = examinations.save(commit=False)
        new_examinations.person = new_person
        if new_examinations.weight and new_examinations.length:
            new_examinations.body_mass=new_examinations.weight / (( new_examinations.length / 100) ** 2 )
        if new_examinations.local_sym_kahesh_vazn == True:
            e_items += "???????? ??????/"
        if new_examinations.local_sym_kahesh_eshteha == True:
            e_items += "???????? ??????????/"
        if new_examinations.local_sym_khastegi == True:
            e_items += "?????????? ????????/"
        if new_examinations.local_sym_ekhtelal_dar_khab == True:
            e_items += "???????????? ???? ????????/"
        if new_examinations.local_sym_tarigh == True:
            e_items += "?????????? ?????? ???? ????/"
        if new_examinations.local_sym_adam_tahamol == True:
            e_items += "?????? ???????? ???????? ?? ????????/"
        if new_examinations.local_sym_tab == True:
            e_items += "????/"
        if new_examinations.local_sign_zaheri == True:
            e_items += "?????????? ??????????/"
        if new_examinations.local_sign_rang_paride == True:
            e_items += "???????????? ?????? ??????????/"
        if new_examinations.local_des:
            e_items += new_examinations.local_des
            e_items += '/'
        if new_examinations.eye_sym_kahesh_binayi == True:
            e_items += "???????? ???? ????????????/"
        if new_examinations.eye_sym_tari_did == True:
            e_items += "???????? ??????/"
        if new_examinations.eye_sym_khastegi == True:
            e_items += "?????????? ??????/"
        if new_examinations.eye_sym_dobini == True:
            e_items += "????????????/"
        if new_examinations.eye_sym_sozesh == True:
            e_items += "???????? ??????/"
        if new_examinations.eye_sym_tars_az_nor == True:
            e_items += "?????? ???? ??????/"
        if new_examinations.eye_sym_ashk == True:
            e_items += "?????? ????????/"
        if new_examinations.eye_sign_reflex == True:
            e_items += "?????????? ?????? ?????????? ??????????/"
        if new_examinations.eye_sign_red == True:
            e_items += "?????????? ??????/"
        if new_examinations.eye_sign_sklrai == True:
            e_items += "?????????????? ??????????????/"
        if new_examinations.eye_sign_nistagemos == True:
            e_items += "??????????????????/"
        if new_examinations.eye_des:
            e_items += new_examinations.eye_des
            e_items += '/'
        if new_examinations.skin_sym_kharesh_post == True:
            e_items += "???????? ????????/"
        if new_examinations.skin_sym_rizesh_mo == True:
            e_items += "???????? ????/"
        if new_examinations.skin_sym_red == True:
            e_items += "?????????? ????????/"
        if new_examinations.skin_sym_taghir_post == True:
            e_items += "?????????? ?????? ????????/"
        if new_examinations.skin_sym_zakhm == True:
            e_items += "?????? ????????/"
        if new_examinations.skin_sym_poste_rizi == True:
            e_items += "?????????? ????????/"
        if new_examinations.skin_sym_taghir_nakhon == True:
            e_items += "?????????? ?????? ????????/"
        if new_examinations.skin_sign_makol == True:
            e_items += "??????????/"
        if new_examinations.skin_sign_papol == True:
            e_items += "??????????/"
        if new_examinations.skin_sign_nadol == True:
            e_items += "????????/"
        if new_examinations.skin_sign_vezikol == True:
            e_items += "????????????/"
        if new_examinations.skin_sign_zakhm == True:
            e_items += "??????/"
        if new_examinations.skin_sign_kahir == True:
            e_items += "????????/"
        if new_examinations.skin_sign_klabing == True:
            e_items += "??????????????/"
        if new_examinations.skin_sign_rizesh_mantaghe == True:
            e_items += "???????? ?????????? ???? ????/"
        if new_examinations.skin_sign_rizesh_general == True:
            e_items += "???????? ?????????? ????/"
        if new_examinations.skin_sign_taghirat_peygmani == True:
            e_items += "?????????????? ??????????????/"
        if new_examinations.skin_des:
            e_items += new_examinations.skin_des
            e_items += "/"
        if new_examinations.gosh_sym_kahesh_shenavaii == True:
            e_items += "???????? ????????????/"
        if new_examinations.gosh_sym_vez_vez_gosh == True:
            e_items += "???????? ??????/"
        if new_examinations.gosh_sym_sargije == True:
            e_items += "???????????? ??????????/"
        if new_examinations.gosh_sym_dard_gosh == True:
            e_items += "?????? ??????/"
        if new_examinations.gosh_sym_tarashoh_gosh == True:
            e_items += "???????? ??????/"
        if new_examinations.gosh_sym_gereftegi_seda == True:
            e_items += "???????????? ??????/"
        if new_examinations.gosh_sym_galodard == True:
            e_items += "????????????/"
        if new_examinations.gosh_sym_abrrizesh_bini == True:
            e_items += "???????????? ????????/"
        if new_examinations.gosh_sym_ekhtelal_boyayi == True:
            e_items += "???????????? ????????????/"
        if new_examinations.gosh_sym_khareshvsozesh == True:
            e_items += "???????? ?? ???????? ????????/"
        if new_examinations.gosh_sym_khonrizi == True:
            e_items += "?????????????? ????????/"
        if new_examinations.gosh_sym_khoshki == True:
            e_items += "???????? ????????/"
        if new_examinations.gosh_sym_ehsas == True:
            e_items += "?????????? ?????? ???????? ???? ????????/"
        if new_examinations.gosh_sign_eltehab_parde == True:
            e_items += "???????????? ???????? ??????????/"
        if new_examinations.gosh_sign_paregi == True:
            e_items += "?????????? ???????? ??????????/"
        if new_examinations.gosh_sign_afzayesh == True:
            e_items += "???????????? ?????? ?????????? ??????????/"
        if new_examinations.gosh_sign_tarashoh == True:
            e_items += "???????? ?????? ??????/"
        if new_examinations.gosh_sign_egzodai == True:
            e_items += "?????????????? ??????/"
        if new_examinations.gosh_sign_red == True:
            e_items += "?????????? ??????/"
        if new_examinations.gosh_sign_polip == True:
            e_items += "?????????? ????????/"
        if new_examinations.gosh_sign_tndrs == True:
            e_items += "???????????? ?????????? ????/"
        if new_examinations.gosh_sign_lead == True:
            e_items += "lead line/"
        if new_examinations.gosh_sign_bad_smell == True:
            e_items += "?????? ???? ????????/"
        if new_examinations.gosh_sign_eltehab_lase == True:
            e_items += "???????????? ??????/"
        if new_examinations.gosh_sign_zakhm == True:
            e_items += "????????????????????/?????? ??????????/"
        if new_examinations.gosh_des:
            e_items += new_examinations.gosh_des
            e_items += "/"
        if new_examinations.sar_sym_dard_gardan == True:
            e_items += "?????? ????????/"
        if new_examinations.sar_sym_tode_gardani == True:
            e_items += "???????? ??????????/"
        if new_examinations.sar_sign_bozorgi_tiroid == True:
            e_items += "?????????? ??????????????/"
        if new_examinations.sar_sign_gardani == True:
            e_items += "?????????????????????? ??????????/"
        if new_examinations.sar_des:
            e_items += new_examinations.sar_des
            e_items += "/"
        if new_examinations.rie_sym_sorfe == True:
            e_items += "????????/"
        if new_examinations.rie_sym_khelt == True:
            e_items += "??????/"
        if new_examinations.rie_sym_tangi == True:
            e_items += "???????? ?????? ????????/"
        if new_examinations.rie_sym_sine == True:
            e_items += "???? ???? ????????/"
        if new_examinations.rie_sign_zaheri == True:
            e_items += "?????????? ?????????? ?????? ?????????? ???????? ????????/"
        if new_examinations.rie_sign_khoshonat == True:
            e_items += "?????????? ??????/"
        if new_examinations.rie_sign_vizing == True:
            e_items += "????????????/"
        if new_examinations.rie_sign_cracel == True:
            e_items += "??????????/"
        if new_examinations.rie_sign_taki_pene == True:
            e_items += "???????? ??????/"
        if new_examinations.rie_sign_kahesh_sedaha == True:
            e_items += "???????? ???????????? ????????/"
        if new_examinations.rie_des:
            e_items += new_examinations.rie_des
            e_items += "/"
        if new_examinations.ghalb_sym_dard == True:
            e_items += "?????? ???????? ????????/"
        if new_examinations.ghalb_sym_tapesh == True:
            e_items += "?????? ??????/"
        if new_examinations.ghalb_sym_tangi_shabane == True:
            e_items += "???????? ?????? ?????????????? ??????????/"
        if new_examinations.ghalb_sym_tangi_khabide == True:
            e_items += "???????? ?????? ?????????????? ??????????????/"
        if new_examinations.ghalb_sym_sianoz == True:
            e_items += "????????????/"
        if new_examinations.ghalb_sym_senkop == True:
            e_items += "?????????? ??????????/"
        if new_examinations.ghalb_sign_s == True:
            e_items += "S1S2?????? ??????????/"
        if new_examinations.ghalb_sign_seda_ezafe == True:
            e_items += "???????? ?????????? ??????/"
        if new_examinations.ghalb_sign_aritmi == True:
            e_items += "????????????/"
        if new_examinations.ghalb_sign_varis_tahtani == True:
            e_items += "?????????? ?????????? ????????????/"
        if new_examinations.ghalb_sign_varis_foghani == True:
            e_items += "?????????? ?????????? ????????????/"
        if new_examinations.ghalb_sign_andam == True:
            e_items += "?????? ??????????/"
        if new_examinations.ghalb_des:
            e_items += new_examinations.ghalb_des
            e_items += "/"
        if new_examinations.shekam_sym_bi_eshteha == True:
            e_items += "???? ??????????????/"
        if new_examinations.shekam_sym_tahavo == True:
            e_items += "????????/"
        if new_examinations.shekam_sym_estefragh == True:
            e_items += "??????????????/"
        if new_examinations.shekam_sym_dard_shekam == True:
            e_items += "?????? ??????/"
        if new_examinations.shekam_sym_soozesh == True:
            e_items += "???????? ???? ????/"
        if new_examinations.shekam_sym_eshal == True:
            e_items += "??????????/"
        if new_examinations.shekam_sym_yobosat == True:
            e_items += "??????????/"
        if new_examinations.shekam_sym_ghiri == True:
            e_items += "?????????? ????????/"
        if new_examinations.shekam_sym_roshan == True:
            e_items += "?????? ???????? ???? ??????????/"
        if new_examinations.shekam_sym_ekhtelal == True:
            e_items += "???????????? ???? ??????/"
        if new_examinations.shekam_sign_shekami == True:
            e_items += "???????????? ????????/"
        if new_examinations.shekam_sign_rebond == True:
            e_items += "???????????? ????????????/"
        if new_examinations.shekam_sign_hepatomegaly == True:
            e_items += "????????????????????/"
        if new_examinations.shekam_sign_espelnomegali == True:
            e_items += "??????????????????????/"
        if new_examinations.shekam_sign_asib == True:
            e_items += "????????/"
        if new_examinations.shekam_sign_tode_shekami == True:
            e_items += "???????? ????????/"
        if new_examinations.shekam_sign_distansion == True:
            e_items += "???????????????????? ????????/"
        if new_examinations.shekam_des:
            e_items += new_examinations.shekam_des
            e_items += "/"
        if new_examinations.colie_sym_soozesh == True:
            e_items += "???????? ????????/"
        if new_examinations.colie_sym_tekrar == True:
            e_items += "???????? ??????????/"
        if new_examinations.colie_sym_khoni == True:
            e_items += "?????????? ????????/"
        if new_examinations.colie_sym_pahlo == True:
            e_items += "?????? ????????/"
        if new_examinations.colie_sym_sangini == True:
            e_items += "?????????? ???????????? ???? ???????? ???? ????????/"
        if new_examinations.colie_sign_cva == True:
            e_items += "??????????????CVA/"
        if new_examinations.colie_sign_varikosel == True:
            e_items += "????????????????/"
        if new_examinations.colie_des:
            e_items += new_examinations.colie_des
            e_items += "/"
        if new_examinations.eskelety_sym_mafsal == True:
            e_items += "???????? ????????/"
        if new_examinations.eskelety_sym_kamar_dard == True:
            e_items += "????????????/"
        if new_examinations.eskelety_sym_zano == True:
            e_items += "?????? ????????/"
        if new_examinations.eskelety_sym_shane == True:
            e_items += "?????? ????????/"
        if new_examinations.eskelety_sym_other_mafasel == True:
            e_items += "?????? ???????? ??????????/"
        if new_examinations.eskelety_sign_mahdodiat == True:
            e_items += "?????????????? ?????????? ????????/"
        if new_examinations.eskelety_sign_kahesh_foghani == True:
            e_items += "???????? ???????? ???????????? ???? ?????????? ????????????/"
        if new_examinations.eskelety_sign_kahesh_tahtani == True:
            e_items += "???????? ???????? ???????????? ???? ?????????? ????????????/"
        if new_examinations.eskelety_sign_eskolioz == True:
            e_items += "????????????????/"
        if new_examinations.eskelety_sign_empotasion == True:
            e_items += "????????????????????/"
        if new_examinations.eskelety_sign_slr == True:
            e_items += "?????? SLR ????????/"
        if new_examinations.eskelety_sign_r_slr == True:
            e_items += "?????? Reverse-SLR/"
        if new_examinations.eskelety_des:
            e_items += new_examinations.eskelety_des
            e_items += "/"
        if new_examinations.asabi_sym_sar_dard == True:
            e_items += "??????????/"
        if new_examinations.asabi_sym_giji == True:
            e_items += "????????/"
        if new_examinations.asabi_sym_larzesh == True:
            e_items += "????????/"
        if new_examinations.asabi_sym_ekhtelal == True:
            e_items += "???????????? ??????????/"
        if new_examinations.asabi_sym_tashanoj == True:
            e_items += "?????????? ??????/????????/"
        if new_examinations.asabi_sym_gez_gez == True:
            e_items += "???? ???? ?? ?????? ?????? ?????????????? ??????/"
        if new_examinations.asabi_sign_tabi_e == True:
            e_items += "?????????? ?????????? ?????? ??????????/"
        if new_examinations.asabi_sign_gheir_tabi_e == True:
            e_items += "?????????? ???????? ????????????????/"
        if new_examinations.asabi_sign_mokhtal == True:
            e_items += "?????? ???????????? ????????/"
        if new_examinations.asabi_sign_trmor == True:
            e_items += "??????????/"
        if new_examinations.asabi_sign_hesi == True:
            e_items += "???????????? ?????? ?????????? ????/"
        if new_examinations.asabi_sign_tinel == True:
            e_items += "?????? ???????? ????????/"
        if new_examinations.asabi_sign_falen == True:
            e_items += "?????? ???????? ????????/"
        if new_examinations.asabi_des:
            e_items += new_examinations.asabi_des 
            e_items += "/"
        if new_examinations.ravan_sym_asabaniat == True:
            e_items += "?????????????? ?????? ???? ????/"
        if new_examinations.ravan_sym_parkhashgari == True:
            e_items += "????????????????/"
        if new_examinations.ravan_sym_ezterab == True:
            e_items += "????????????/"
        if new_examinations.ravan_sym_kholgh == True:
            e_items += "?????? ??????????/"
        if new_examinations.ravan_sym_angize == True:
            e_items += "???????? ????????????/"
        if new_examinations.ravan_sign_hazyan == True:
            e_items += "??????????/"
        if new_examinations.ravan_sign_tavahom == True:
            e_items += "????????/"
        if new_examinations.ravan_sign_oriantasion == True:
            e_items += "???????????? ????????????????????????/"
        if new_examinations.ravan_des:
            e_items += new_examinations.ravan_des
            e_items += "/" 
        new_examinations.not_normals = e_items    
        new_examinations.save()
    if personal_species.is_valid() and  experiments.is_valid():
        new_experiments = experiments.save(commit=False)
        new_experiments.person = new_person
        if new_experiments.cbc_wbc:
            if new_experiments.cbc_wbc < 4 and new_experiments.cbc_wbc >10:
                new_experiments.cbc_wbc_status = False 
        else:
            new_experiments.cbc_wbc_status = True
        if new_experiments.cbc_plt:
            if new_experiments.cbc_plt < 140 and new_experiments.cbc_plt >450:
                    new_experiments.cbc_plt_status = False 
        else:
            new_experiments.cbc_plt_status = True
        if new_experiments.ua_prot:
            if new_experiments.ua_prot < 0 and new_experiments.ua_prot >0:
                    new_experiments.ua_prot_status = False
        else:
            new_experiments.ua_prot_status = True
        if new_experiments.ua_glu:
            if new_experiments.ua_glu < 0 and new_experiments.ua_glu >0:
                    new_experiments.ua_glu_status = False 
        else:
            new_experiments.ua_glu_status = True
        if new_experiments.ua_rbc:
            if new_experiments.ua_rbc > 3:
                new_experiments.ua_rbc_status = False 
        else:
            new_experiments.ua_rbc_status = True
        if new_experiments.ua_wbc:
            if new_experiments.ua_wbc > 5:
                new_experiments.ua_wbc_status = False 
        else:
            new_experiments.ua_wbc_status = True
        if new_experiments.ua_bact:
            if new_experiments.ua_bact < 0 and new_experiments.ua_bact > 0:
                new_experiments.ua_bact_status = False 
        else:
            new_experiments.ua_bact_status = True
        if new_experiments.fbs:
            if new_experiments.fbs < 70 and new_experiments.fbs > 125:
                new_experiments.fbs_status = False 
        else:
            new_experiments.fbs_status = True
        if new_experiments.chol:
            if new_experiments.chol > 200:
                new_experiments.chol_status = False 
        else:
            new_experiments.chol_status = True
        if new_experiments.ldl:
            if new_experiments.ldl >100:
                new_experiments.ldl_status = False 
        else:
            new_experiments.ldl_status = True
        if new_experiments.tsh:
            if new_experiments.tsh < 0.4 and new_experiments.tsh > 5:
                new_experiments.tsh_status = False  
        else:
            new_experiments.tsh_status = True
        if new_experiments.tg:
            if new_experiments.tg > 200:
                    new_experiments.tg_status = False 
        else:
            new_experiments.tg_status = True
        if new_experiments.cr:
            if new_experiments.cr >= 1.4:
                new_experiments.cr_status = False 
        else:
            new_experiments.cr_status = True
        if new_experiments.alt:
            if new_experiments.alt >= 40:
                new_experiments.alt_status = False 
        else:
            new_experiments.alt_status = True
        if new_experiments.ast:
            if new_experiments.ast >= 40:
                new_experiments.ast_status = False 
        else:
            new_experiments.ast_status = True
        if new_experiments.ast:
            if new_experiments.alk < 14 and new_experiments.alk > 20:
                    new_experiments.alk_status = False 
        else:
            new_experiments.alk_status = True
        if new_experiments.lead:
            if ew_experiments.lead > 20:
                new_experiments.lead_status = False 
        else:
            new_experiments.lead_status = True
        if new_experiments.d:
            if new_experiments.d <= 30 and new_experiments.d >101:
                new_experiments.d_status = False  
        else:
            new_experiments.d_status = True
        if new_experiments.psa:
            if new_person.age < 40:
                if new_experiments.psa >= 1.7:
                    new_experiments.psa_status = False
            if new_person.age < 50 and new_person.age >= 40 :
                if new_experiments.psa >= 2.2:
                    new_experiments.psa_status = False
            if nnew_person.age < 60 and new_person.age >= 50:
                if new_experiments.psa >= 3.4:
                    new_experiments.psa_status = False
            if new_person.age < 70 and new_person.age >= 60:
                if new_experiments.psa >= 6.16:
                    new_experiments.psa_status = False
            if new_person.age > 70:
                if new_experiments.psa >= 6.77:
                    new_experiments.psa_status = False
        else:
            new_experiments.psa_status = True
        if new_person.gender == 'mard':
            if new_experiments.cbc_rbc:
                if new_experiments.cbc_rbc < 4 and new_experiments.cbc_rbc >5.5:
                    new_experiments.cbc_rbc_status = False 
            else:
                new_experiments.cbc_rbc_status = True
            if new_experiments.cbc_hb:
                if new_experiments.cbc_hb < 12 and new_experiments.cbc_hb >16:
                    new_experiments.cbc_hb_status = False 
            else:
                new_experiments.cbc_hb_status = True
            if new_experiments.cbc_htc:
                if new_experiments.cbc_htc < 40 and new_experiments.cbc_htc >54:
                    new_experiments.cbc_htc_status = False 
            else:
                new_experiments.cbc_htc_status = True
            if new_experiments.hdl:
                if new_experiments.hdl > 40:
                    new_experiments.hdl_status = False    
            else:
                new_experiments.hdl_status = True 
        if new_person.gender == 'zan':
            if new_experiments.cbc_rbc:
                if new_experiments.cbc_rbc < 3.5 and new_experiments.cbc_rbc >5:
                    new_experiments.cbc_rbc_status = False 
            else:
                new_experiments.cbc_rbc_status = True
            if new_experiments.cbc_hb:
                if new_experiments.cbc_hb < 11 and new_experiments.cbc_hb >15:
                    new_experiments.cbc_hb_status = False 
            else:
                new_experiments.cbc_hb_status = True
            if new_experiments.cbc_htc:
                if new_experiments.cbc_htc < 37 and new_experiments.cbc_htc >47:
                    new_experiments.cbc_htc_status = False 
            else:
                new_experiments.cbc_htc_status = True
            if new_experiments.hdl:
                if new_experiments.hdl > 50:
                    new_experiments.hdl_status = False    
            else:
                new_experiments.hdl_status = True      
        new_experiments.save()
    if personal_species.is_valid() and  para_clinic.is_valid():
        new_para_clinic = para_clinic.save(commit=False)
        new_para_clinic.person = new_person
        new_para_clinic.save()
    if personal_species.is_valid() and  consulting.is_valid():
        new_consulting = consulting.save(commit=False)
        new_consulting.person = new_person
        new_consulting.save()
    if personal_species.is_valid() and  final_theory.is_valid():
        new_final_theory = final_theory.save(commit=False)
        new_final_theory.person = new_person
        new_final_theory.save()
    return redirect('examinations')


@login_required(login_url='login')
def examinations_output_view(request):
    form=disease_form()
    model=Disease_Model.objects.last()
    if model:
        code=model.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(name=model.name,age=model.age,fathers_name=model.fathers_name,personal_code=model.personal_code,examinations_code=examinations_course).last()
    job_history=Job_History_Model.objects.filter(person=personal_species).last()
    assessment=Assessment_Model.objects.filter(person=personal_species).last()
    personal_history=Personal_History_Model.objects.filter(person=personal_species).last()
    examinations=Examinations_Model.objects.filter(person=personal_species).last()
    experiments=Experiments_Model.objects.filter(person=personal_species).last()
    para_clinic=Para_Clinic_Model.objects.filter(person=personal_species).last()
    consulting=Consulting_Model.objects.filter(person=personal_species).last()
    final_theory=Final_Theory_Model.objects.filter(person=personal_species).last()
    context={'form':form, 'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory }
    return render(request, 'examinations_output.html',context)


def examinations_output_pdf_view(request):
    work=Disease_Model.objects.last()
    if work:
        code=work.examinations_code
    else:
        code=''
    examinations_course = ExaminationsCourse.objects.filter(examinations_code=code).last()
    personal_species=Personal_Species_Model.objects.filter(examinations_code=examinations_course)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('F:\parsian\chromedriver',options=options)
    driver.get("http://127.0.0.1:8000/login")
    username = driver.find_element('name',"username")
    password = driver.find_element('name',"password")
    login_but = driver.find_element('name',"login")
    username.send_keys('parsa')
    password.send_keys('690088choose')
    login_but.click()
    driver.get("http://127.0.0.1:8000/output/examinations_output")
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(1920,S('Height'))
    count = 0
    i = 0
    pdf = FPDF()
    driver.find_element('id','examinations0').screenshot('images/examinations0.png')
    pdf.add_page()
    pdf.image('images/examinations0.png',4,None,200,240)
    os.remove('images/examinations0.png')
    driver.find_element('id','examinations1').screenshot('images/examinations1.png')
    pdf.add_page()
    pdf.image('images/examinations1.png',4,None,200,180)
    os.remove('images/examinations1.png')
    driver.find_element('id','examinations2').screenshot('images/examinations2.png')
    pdf.add_page()
    pdf.image('images/examinations2.png',10,None,180,265)
    os.remove('images/examinations2.png')
    driver.find_element('id','examinations3').screenshot('images/examinations3.png')
    pdf.add_page()
    pdf.image('images/examinations3.png',4,None,200,265)
    os.remove('images/examinations3.png')
    driver.find_element('id','examinations4').screenshot('images/examinations4.png')
    pdf.add_page()
    pdf.image('images/examinations4.png',4,None,200,140)
    os.remove('images/examinations4.png')
    pdf.output("pdfs/examinations.pdf", "F")
    file_path = os.path.join('pdfs/examinations.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@require_POST
def addexaminations_output_view(request):
    model=Disease_Model.objects.last()
    form=disease_form(request.POST)
    if form.is_valid():
        model.name=form.cleaned_data['name']
        model.fathers_name=form.cleaned_data['fathers_name']
        model.age=form.cleaned_data['age']
        model.personal_code=form.cleaned_data['personal_code']
        model.save()
    return redirect('examinations_output')
