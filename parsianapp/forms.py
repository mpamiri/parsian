from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results,submit_company
from . import models
class registration(UserCreationForm):
    class meta:
        model=User
        fields=['username','password']


class summary_of_results_form(forms.ModelForm):
    class Meta:
        model = summary_of_results
        fields = '__all__'
        widgets={
        'code' : forms.Select(attrs={'class':'box','autocomplete': 'off'})
        ,'gender' : forms.Select(attrs={'class':'box','autocomplete': 'off'})
        ,'number' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'start_month' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'start_year' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'age' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'length' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'weight' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'blood_sugar' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'blood_pressure' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'cholesterol' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'triglyceride' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'blood_lead' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'chratinin' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'ALT' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'AST' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'PSA' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'TSH' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'D3' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'job_code' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'right_eye_vision' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'right_eye_vision_with_glasses' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'left_eye_vision' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'left_eye_vision_with_glasses' : forms.NumberInput(attrs={'class':'box','autocomplete': 'off'})
        ,'urine' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'breathing_test' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'breast_photo' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'heart' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'color_vision' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'field_of_veiw' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'depth_vision' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'right_ear_hearing' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'left_ear_hearing' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'problems_with_the_persons_job' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'refer_to_specialist' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'final_theory' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'occupational_actions' : forms.Select(attrs={'class':'choose','autocomplete': 'off'})
        ,'examinations_code' : forms.TextInput(attrs={'id':'myInput','onkeyup':"filterFunction()",'autocomplete': 'off'})
        ,'name' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'job' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'harmful_factors' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'body_mass' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'body_mass_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'blood_sugar_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'blood_pressure_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'cholesterol_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'triglyceride_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'left_eye_vision_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'right_eye_vision_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'blood_lead_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'PSA_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'TSH_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'problem' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'recommendations' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'reson_for_opening_the_case' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'occupational_disease_code' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'AST_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'ALT_status' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'duration_of_employment' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'overweight' : forms.TextInput(attrs={'autocomplete': 'off'})}

class submit_company_form(forms.ModelForm):
    class Meta:
        model = submit_company
        fields = '__all__'
        widgets={
        'company' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'doctor' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'specialist' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'date' : forms.TextInput(attrs={'autocomplete': 'off'})
        ,'examinations_code' : forms.TextInput(attrs={'autocomplete': 'off'})}
