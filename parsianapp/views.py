from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Summary_Of_Results_Model,Submit_Company_Model,Disease_Model,Personal_Species_Model,Job_History_Model,Assessment_Model,Personal_History_Model,Examinations_Model,Experiments_Model,Para_Clinic_Model,Consulting_Model,Final_Theory_Model,ExaminationsCourse
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
    if Disease_Model.DoesNotExist():
        new_disease = Disease_Model(examinations_code='',order_number= 1)
        new_disease.save()
        model=Disease_Model.objects.get(pk=1)
    else:
        model=Disease_Model.objects.get(pk=1)
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
    items=[]
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory, 'examinations_course':examinations_course}
    return render(request, 'disease_code.html',context)

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
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'examinations_course':examinations_course}
    return render(request, 'graph.html',context)

@login_required(login_url='login')
def solo_output_view(request):
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
    company=Submit_Company_Model.objects.all()
    if work:
        number=work.order_number
    else:
        number='1'
    p = Paginator(Summary_Of_Results_Model.objects.filter(examinations_code=code),number)
    page=request.GET.get('page')
    solo_page=p.get_page(page)
    nums='a' * solo_page.paginator.num_pages
    initial_dict = {
        'order_number':number       
    }
    form=disease_form(initial=initial_dict)
    context={'personal_species' : personal_species , 'job_history' : job_history , 'assessment' : assessment, 'personal_history' : personal_history, 'examinations' : examinations, 'experiments' : experiments, 'para_clinic' : para_clinic, 'consulting' : consulting , 'final_theory' : final_theory,'form' :form,'examinations_course' : examinations_course}
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
            items += ' سر و صدا/'
        if new_assessment.current_ph_erteash == True:
            items += ' ارتعاش/'
        if new_assessment.current_ph_not_unizan == True:
            items += ' اشعه غیر یونیزان/'
        if new_assessment.current_ph_unizan == True:
            items += ' اشعه یونیزان/'
        if new_assessment.current_ph_stress == True:
            items += ' استرس حرارتی/'
        if new_assessment.current_sh_dust == True:
            items += ' گرد و غبار/'
        if new_assessment.current_sh_metals == True:
            items += ' دمه فلزات/'
        if new_assessment.current_sh_halal == True:
            items += ' حلال/'
        if new_assessment.current_sh_afat == True:
            items += ' آفت کشها/'
        if new_assessment.current_sh_asidvbaz == True:
            items += ' اسید و بازها/'
        if new_assessment.current_sh_gaz == True:
            items += ' گاز ها/'
        if new_assessment.current_bio_gazesh == True:
            items += ' گزش/'
        if new_assessment.current_bio_bactery == True:
            items += ' باکتری/'
        if new_assessment.current_bio_virus == True:
            items += ' ویروس/'
        if new_assessment.current_bio_angal == True:
            items += ' انگل/'
        if new_assessment.current_er_standvsit == True:
            items += ' ایستادن یا نشستن طولانی مدت/'
        if new_assessment.current_er_loop == True:
            items += ' کار تکراری/'
        if new_assessment.current_er_hamlvnaghl == True:
            items += ' حمل و نقل بار سنگین/'
        if new_assessment.current_er_vaziat_namonaseb == True:
            items += ' وضعیت نامناسب بدن/'
        if new_assessment.current_rav_order == True:
            items += ' نوبت کاری/'
        if new_assessment.current_rav_stressor == True:
            items += ' استرسور های شغلی/'  
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
