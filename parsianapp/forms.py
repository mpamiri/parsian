from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Disease_Model,Personal_Species_Model,Job_History_Model,Assessment_Model,Personal_History_Model,Examinations_Model,Experiments_Model,Para_Clinic_Model,Consulting_Model,Final_Theory_Model,Company,ExaminationsCourse
from . import models
from django.core.validators import MaxValueValidator, MinValueValidator 
class registration(UserCreationForm):
    class meta:
        model=User
        fields=['username','password']

        
class submit_company_form(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets={
        'company' : forms.TextInput(attrs={'autocomplete': 'off' , })}

class ExaminationsCompanyChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.name

class submit_course_form(forms.ModelForm):
    company : ExaminationsCompanyChoiceField(queryset=Company.objects.all())
    class Meta:
        model = ExaminationsCourse
        fields = '__all__'
        widgets={
        'year' : forms.TextInput(attrs={'autocomplete': 'off' }),
        'doctor' : forms.TextInput(attrs={'autocomplete': 'off' }),
        'employer' : forms.TextInput(attrs={'autocomplete': 'off' }),
        'examinations_code' : forms.TextInput(attrs={'autocomplete': 'off' })}

class disease_form(forms.ModelForm):
    class Meta:
        model=Disease_Model
        fields='__all__'
        widgets={'examinations_code' : forms.TextInput(attrs={'id':'myInput','onkeyup':"filterFunction()",'autocomplete': 'off'})
        ,'order_number' : forms.Select(attrs={'autocomplete': 'off'})
        ,'age' : forms.NumberInput(attrs={'autocomplete': 'off'})
        ,'name' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'fathers_name' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'personal_code' : forms.NumberInput(attrs={'autocomplete': 'off'})
        }  

class ExaminationsCourseChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.examinations_code

class personal_species_form(forms.ModelForm):
    examinations_code = ExaminationsCourseChoiceField(queryset=ExaminationsCourse.objects.all())
    class Meta:
        model=Personal_Species_Model
        fields='__all__' 
        widgets={
        'date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'examinations_type' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'profil_number' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'employment_number' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'name' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'fathers_name' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'gender' : forms.Select(attrs={'class':'s_box','autocomplete': 'off','id':'select'}),
        'marriage_status' : forms.Select(attrs={'class':'box','autocomplete': 'off'}),
        'children' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'age' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'personal_code' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'military_status' : forms.Select(attrs={'class':'text','autocomplete': 'off'}),
        'raste' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'medical_exemption_reason' : forms.TextInput(attrs={'class':'text','autocomplete': 'off' ,'disabled':'disabled'}),
        'job_name' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'employer_name' : forms.TextInput(attrs={'class':'text','autocomplete': 'off'}),
        'address' : forms.TextInput(attrs={'style':'width : 800px','autocomplete': 'off'}),
        'date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }

class job_history_form(forms.ModelForm):
    class Meta:
        model=Job_History_Model
        fields='__all__' 
        widgets={
        'current_job' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'current_job_duty' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'current_job_from_year' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_from_month' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_from_day' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_to_year' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_to_month' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_to_day' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'}),
        'current_job_reason' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_current_job' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_current_job_duty' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_current_job_from' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_current_job_to' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_current_job_reason' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'previous_job' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'previous_job_duty' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'previous_job_from' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'previous_job_to' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'previous_job_reason' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_previous_job' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_previous_job_duty' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_previous_job_from' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_previous_job_to' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'}),
        'second_previous_job_reason' : forms.TextInput(attrs={'class':'text remove','autocomplete': 'off'})
        }

class assessment_form(forms.ModelForm):
    class Meta:
        model=Assessment_Model
        fields='__all__' 
        widgets={
        'date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }
        
class personal_history_form(forms.ModelForm):
    class Meta:
        model=Personal_History_Model
        fields='__all__' 

class examinations_form(forms.ModelForm):
    class Meta:
        model=Examinations_Model
        fields='__all__' 
        widgets={
        'weight' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'blood_pressure' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'length' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'pulse' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }

class experiments_form(forms.ModelForm):
    class Meta:
        model=Experiments_Model
        fields='__all__' 
        widgets={
        'cbc_wbc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'cbc_rbc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'cbc_hb' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'cbc_htc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'cbc_plt' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ua_prot' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ua_glu' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ua_rbc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ua_wbc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ua_bact' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'fbs' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'chol' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ldl' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'hdl' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'tg' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'lead' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'cr' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'alt' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'd' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'tsh' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'ast' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'alk' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'psa' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'se_status' : forms.Select(attrs={'class':'s_box','autocomplete': 'off'}),
        'ppd_status' : forms.Select(attrs={'class':'s_box','autocomplete': 'off'}),
        'first_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'first_date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'first_date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'third_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'third_date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'third_date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }

class para_clinic_form(forms.ModelForm):
    class Meta:
        model=Para_Clinic_Model
        fields='__all__' 
        widgets={
        'opto_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_hedat_r_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off','disabled':'disabled'}),
        'opto_hedat_r_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off','disabled':'disabled'}),
        'opto_hedat_r_status' : forms.Select(attrs={'autocomplete': 'off','onchange':"toggleInput();"}),
        'opto_hedat_l_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off','disabled':'disabled'}),
        'opto_hedat_l_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off','disabled':'disabled'}),
        'opto_hedat_l_status' : forms.Select(attrs={'autocomplete': 'off','onchange':"toggleInput();"}),
        'opto_rangi_hedat_r_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_rangi_hedat_r_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_rangi_hedat_l_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_rangi_hedat_l_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_meidan_hedat_r_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_meidan_hedat_r_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_meidan_hedat_l_ba' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_meidan_hedat_l_bi' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'opto_omgh' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_tafsir' : forms.Select(attrs={'autocomplete': 'off'}),
        'audio_l_tafsir' : forms.Select(attrs={'autocomplete': 'off'}),
        'audio_date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_eight_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_eight_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_six_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_six_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_four_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_four_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_two_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_two_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_one_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_one_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_five_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_r_five_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_eight_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_eight_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_six_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_six_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_four_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_four_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_two_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_two_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_one_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_one_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_five_ac' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'audio_l_five_bc' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'espiro_date_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'espiro_date_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'espiro_date_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'espiro_tafsir' : forms.Select(attrs={'autocomplete': 'off'}),
        'other_cxr_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'other_cxr_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'other_cxr_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'other_ecg_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'other_ecg_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'other_ecg_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }

class consulting_form(forms.ModelForm):
    class Meta:
        model=Consulting_Model
        fields='__all__' 
        widgets={
        'first_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'first_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'first_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_year' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_month' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'}),
        'second_day' : forms.NumberInput(attrs={'class':'s_box','autocomplete': 'off'})
        }

class final_theory_form(forms.ModelForm):
    class Meta:
        model=Final_Theory_Model
        fields='__all__' 
        widgets={
        'mashrot_reason' : forms.TextInput(attrs={'autocomplete': 'off'}),
        'rad_reason' : forms.TextInput(attrs={'autocomplete': 'off'}),
        'recommendations' : forms.TextInput(attrs={'autocomplete': 'off'}),
        'reason' : forms.TextInput(attrs={'autocomplete': 'off'}),
        'problems' : forms.TextInput(attrs={'autocomplete': 'off'}),
        'd_code' : forms.NumberInput(attrs={'autocomplete': 'off','class':'box'})
        }




