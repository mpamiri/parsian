from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import summary_of_results
class registration(UserCreationForm):
    class meta:
        model=User
        fields=['username','password']


class summary_of_results(forms.ModelForm):
    class Meta:
        model = summary_of_results
        fields = '__all__'
        widgets={
        'code' : forms.Select(attrs={'class':'box'})
        ,'gender' : forms.Select(attrs={'class':'box'})
        ,'number' : forms.NumberInput(attrs={'class':'box'})
        ,'start_month' : forms.NumberInput(attrs={'class':'box'})
        ,'start_year' : forms.NumberInput(attrs={'class':'box'})
        ,'age' : forms.NumberInput(attrs={'class':'box'})
        ,'length' : forms.NumberInput(attrs={'class':'box'})
        ,'weight' : forms.NumberInput(attrs={'class':'box'})
        ,'blood_sugar' : forms.NumberInput(attrs={'class':'box'})
        ,'blood_pressure' : forms.NumberInput(attrs={'class':'box'})
        ,'cholesterol' : forms.NumberInput(attrs={'class':'box'})
        ,'triglyceride' : forms.NumberInput(attrs={'class':'box'})
        ,'blood_lead' : forms.NumberInput(attrs={'class':'box'})
        ,'chratinin' : forms.NumberInput(attrs={'class':'box'})
        ,'ALT' : forms.NumberInput(attrs={'class':'box'})
        ,'AST' : forms.NumberInput(attrs={'class':'box'})
        ,'PSA' : forms.NumberInput(attrs={'class':'box'})
        ,'TSH' : forms.NumberInput(attrs={'class':'box'})
        ,'D3' : forms.NumberInput(attrs={'class':'box'})
        ,'job_code' : forms.NumberInput(attrs={'class':'box'})
        ,'right_eye_vision' : forms.NumberInput(attrs={'class':'box'})
        ,'right_eye_vision_with_glasses' : forms.NumberInput(attrs={'class':'box'})
        ,'left_eye_vision' : forms.NumberInput(attrs={'class':'box'})
        ,'left_eye_vision_with_glasses' : forms.NumberInput(attrs={'class':'box'})
        ,'urine' : forms.Select(attrs={'class':'choose'})
        ,'breathing_test' : forms.Select(attrs={'class':'choose'})
        ,'breast_photo' : forms.Select(attrs={'class':'choose'})
        ,'heart' : forms.Select(attrs={'class':'choose'})
        ,'color_vision' : forms.Select(attrs={'class':'choose'})
        ,'field_of_veiw' : forms.Select(attrs={'class':'choose'})
        ,'depth_vision' : forms.Select(attrs={'class':'choose'})
        ,'examinations_code_form' : forms.TextInput(attrs={'class':'code'})
        ,'right_ear_hearing' : forms.Select(attrs={'class':'choose'})
        ,'left_ear_hearing' : forms.Select(attrs={'class':'choose'})
        ,'problems_with_the_persons_job' : forms.Select(attrs={'class':'choose'})
        ,'refer_to_specialist' : forms.Select(attrs={'class':'choose'})
        ,'final_theory' : forms.Select(attrs={'class':'choose'})
        ,'occupational_actions' : forms.Select(attrs={'class':'choose'})}
        