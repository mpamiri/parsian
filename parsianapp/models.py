from django.db import models
from django import forms

class summary_of_results(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    number = models.IntegerField(default=0,null=True,blank=True)
    start_month = models.IntegerField(default=0,null=True,blank=True)
    start_year = models.IntegerField(default=0,null=True,blank=True)
    job = models.CharField(max_length=30,null=True,blank=True)
    job_code = models.IntegerField(default=0,null=True,blank=True)
    harmful_factors = models.CharField(max_length=100,null=True,blank=True)
    CODE_CHOICES=[(1,'1'),(2,'2'),(3,'3')]
    code = models.IntegerField(default=1,choices=CODE_CHOICES,null=True,blank=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    length = models.IntegerField(default=0,null=True,blank=True)
    weight = models.IntegerField(default=0,null=True,blank=True)
    body_mass = models.CharField(max_length=300,null=True,blank=True)
    body_mass_status = models.CharField(max_length=300,null=True,blank=True)
    blood_sugar = models.IntegerField(default=0,null=True,blank=True)
    blood_sugar_status = models.CharField(max_length=300,null=True,blank=True)
    blood_pressure = models.IntegerField(default=0,null=True,blank=True)
    blood_pressure_status = models.CharField(max_length=300,null=True,blank=True)
    cholesterol = models.IntegerField(default=0,null=True,blank=True)
    cholesterol_status = models.CharField(max_length=300,null=True,blank=True)
    triglyceride = models.IntegerField(default=0,null=True,blank=True)
    triglyceride_status = models.CharField(max_length=300,null=True,blank=True)
    URINE_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    urine = models.CharField(choices=URINE_CHOICES,max_length=300,default='',null=True,blank=True)
    breathing_CHOICES=[('null',''),('نرمال','نرمال'),('تحدیدی','تحدیدی'),('انسدادی','انسدادی'),('نیاز به تکرار','نیاز به تکرار'),('namaie_toaman','نمای توامان تحدیدی وانسدادی'),('ندارد','ندارد')]
    breathing_test = models.CharField(choices=breathing_CHOICES,max_length=300,default='',null=True,blank=True)
    left_ear_CHOICES=[('null',''),('نرمال','نرمال'),('کاهش شنوایی هدایتی','کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی','کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا','کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی','توامان هدایتی و حسی عصبی'),('ندارد','ندارد')]
    left_ear_hearing = models.CharField(choices=left_ear_CHOICES,max_length=300,default='',null=True,blank=True)
    right_ear_CHOICES=[('null',''),('نرمال','نرمال'),('کاهش شنوایی هدایتی','کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی','کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا','کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی','توامان هدایتی و حسی عصبی'),('ندارد','ندارد')]
    right_ear_hearing = models.CharField(choices=right_ear_CHOICES,max_length=300,default='',null=True,blank=True)
    left_eye_vision = models.IntegerField(default=0,null=True,blank=True)
    left_eye_vision_status = models.CharField(max_length=300,null=True,blank=True)
    left_eye_vision_with_glasses = models.IntegerField(default=0,null=True,blank=True)
    right_eye_vision = models.IntegerField(default=0,null=True,blank=True)
    right_eye_vision_status = models.CharField(max_length=300,null=True,blank=True)
    right_eye_vision_with_glasses = models.IntegerField(default=0,null=True,blank=True)
    color_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('تشخیص رنگ قرمز','تشخیص رنگ قرمز'),('ندارد','ندارد')]
    color_vision = models.CharField(choices=color_CHOICES,max_length=300,default='',null=True,blank=True)
    field_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    field_of_veiw = models.CharField(choices=field_CHOICES,max_length=300,default='',null=True,blank=True)
    depth_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    depth_vision = models.CharField(choices=depth_CHOICES,max_length=300,default='',null=True,blank=True)
    breast_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    breast_photo = models.CharField(choices=breast_CHOICES,max_length=300,default='',null=True,blank=True)
    heart_CHOICES=[('null',''),('نرمال','نرمال'),('تغییرات غیر اختصاصی','تغییرات غیر اختصاصی'),('نیاز به تکرار','نیاز به تکرار'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    heart = models.CharField(choices=heart_CHOICES,max_length=300,default='',null=True,blank=True)
    blood_lead = models.IntegerField(default=0,null=True,blank=True)
    blood_lead_status = models.CharField(max_length=300,null=True,blank=True)
    chratinin = models.IntegerField(default=0,null=True,blank=True)
    PSA = models.IntegerField(default=0,null=True,blank=True)
    PSA_status = models.CharField(max_length=300,null=True,blank=True)
    D3 = models.IntegerField(default=0,null=True,blank=True)
    TSH = models.IntegerField(default=0,null=True,blank=True)
    TSH_status = models.CharField(max_length=300,null=True,blank=True)
    problem = models.CharField(max_length=300,null=True,blank=True)
    problem_CHOICES=[('null',''),('دارد','دارد'),('ندارد','ندارد')]
    problems_with_the_persons_job = models.CharField(choices=problem_CHOICES,max_length=300,default='',null=True,blank=True)
    recommendations = models.CharField(max_length=300,null=True,blank=True)
    refer_CHOICES=[('null',''),('ندارد','ندارد'),('قلب و عروق','قلب و عروق'),('داخلی','داخلی'),('ریه','ریه'),('غدد','غدد'),('سایر','سایر')]
    refer_to_specialist = models.CharField(choices=refer_CHOICES,max_length=300,default='',null=True,blank=True)
    final_CHOICES=[('null',''),('بلامانع','بلامانع'),('تغییر شغل','تغییر شغل'),('مشروط','مشروط'),('کمیسیون','کمیسیون')]
    final_theory = models.CharField(choices=final_CHOICES,max_length=300,default='',null=True,blank=True)
    reson_for_opening_the_case = models.CharField(max_length=300,null=True,blank=True)
    occupational_CHOICES=[('null',''),('درحال پیگیری','درحال پیگیری'),('انجام شده','انجام شده'),('انجام نشده','انجام نشده')]
    occupational_actions = models.CharField(choices=occupational_CHOICES,max_length=300,default='',null=True,blank=True)
    occupational_disease_code = models.CharField(max_length=300,null=True,blank=True)
    AST = models.IntegerField(default=0,null=True,blank=True)
    AST_status = models.CharField(max_length=300,null=True,blank=True)
    ALT = models.IntegerField(default=0,null=True,blank=True)
    ALT_status = models.CharField(max_length=300,null=True,blank=True)
    age_two = models.IntegerField(default=0,null=True,blank=True)
    duration_of_employment = models.CharField(max_length=300,null=True,blank=True)
    overweight = models.CharField(max_length=300,null=True,blank=True)