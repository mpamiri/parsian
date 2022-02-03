from django.db import models
from django import forms

class summary_of_results(models.Model):
    name = models.CharField(max_length=20)
    start_month = models.IntegerField(default=0)
    start_year = models.IntegerField(default=0)
    job = models.CharField(max_length=30)
    harmful_factors = models.CharField(max_length=100)
    CODE_CHOICES=[('1','1'),('2','2'),('3','3')]
    code = models.IntegerField(default=1,choices=CODE_CHOICES)
    age = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    body_mass = models.CharField(max_length=300)
    body_mass_status = models.CharField(max_length=300)
    blood_sugar = models.IntegerField(default=0)
    blood_sugar_status = models.CharField(max_length=300)
    blood_pressure = models.IntegerField(default=0)
    blood_pressure_status = models.CharField(max_length=300)
    cholesterol = models.IntegerField(default=0)
    cholesterol_status = models.CharField(max_length=300)
    triglyceride = models.IntegerField(default=0)
    triglyceride_status = models.CharField(max_length=300)
    URINE_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    urine = models.CharField(choices=URINE_CHOICES,max_length=300,default='')
    breathing_CHOICES=[('null',''),('نرمال','نرمال'),('تحدیدی','تحدیدی'),('انسدادی','انسدادی'),('نیاز به تکرار','نیاز به تکرار'),('namaie_toaman','نمای توامان تحدیدی وانسدادی'),('ندارد','ندارد')]
    breathing_test = models.CharField(choices=breathing_CHOICES,max_length=300,default='')
    left_ear_CHOICES=[('null',''),('نرمال','نرمال'),('کاهش شنوایی هدایتی','کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی','کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا','کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی','توامان هدایتی و حسی عصبی'),('ندارد','ندارد')]
    left_ear_hearing = models.CharField(choices=left_ear_CHOICES,max_length=300,default='')
    right_ear_CHOICES=[('null',''),('نرمال','نرمال'),('کاهش شنوایی هدایتی','کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی','کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا','کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی','توامان هدایتی و حسی عصبی'),('ندارد','ندارد')]
    right_ear_hearing = models.CharField(choices=right_ear_CHOICES,max_length=300,default='')
    left_eye_vision = models.IntegerField(default=0)
    left_eye_vision_status = models.CharField(max_length=300)
    left_eye_vision_with_glasses = models.IntegerField(default=0)
    right_eye_vision = models.IntegerField(default=0)
    right_eye_vision_status = models.CharField(max_length=300)
    right_eye_vision_with_glasses = models.IntegerField(default=0)
    color_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('تشخیص رنگ قرمز','تشخیص رنگ قرمز'),('ندارد','ندارد')]
    color_vision = models.CharField(choices=color_CHOICES,max_length=300,default='')
    field_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    field_of_veiw = models.CharField(choices=field_CHOICES,max_length=300,default='')
    depth_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    depth_vision = models.CharField(choices=depth_CHOICES,max_length=300,default='')
    breast_CHOICES=[('null',''),('نرمال','نرمال'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    breast_photo = models.CharField(choices=breast_CHOICES,max_length=300,default='')
    blood_CHOICES=[('null',''),('نرمال','نرمال'),('تغییرات غیر اختصاصی','تغییرات غیر اختصاصی'),('نیاز به تکرار','نیاز به تکرار'),('غیر نرمال','غیر نرمال'),('ندارد','ندارد')]
    blood_lead = models.CharField(choices=blood_CHOICES,max_length=300,default='')
    blood_lead_status = models.CharField(max_length=300)
    PSA = models.IntegerField(default=0)
    PSA_status = models.CharField(max_length=300)
    TSH = models.IntegerField(default=0)
    TSH_status = models.CharField(max_length=300)
    problem = models.CharField(max_length=300)
    problem_CHOICES=[('null',''),('دارد','دارد'),('ندارد','ندارد')]
    problems_with_the_persons_job = models.CharField(choices=problem_CHOICES,max_length=300,default='')
    recommendations = models.CharField(max_length=300)
    refer_CHOICES=[('null',''),('ندارد','ندارد'),('قلب و عروق','قلب و عروق'),('داخلی','داخلی'),('ریه','ریه'),('غدد','غدد'),('سایر','سایر')]
    refer_to_specialist = models.CharField(choices=refer_CHOICES,max_length=300,default='')
    final_CHOICES=[('null',''),('بلامانع','بلامانع'),('تغییر شغل','تغییر شغل'),('مشروط','مشروط'),('کمیسیون','کمیسیون')]
    final_theory = models.CharField(choices=final_CHOICES,max_length=300,default='')
    reson_for_opening_the_case = models.CharField(max_length=300)
    occupational_CHOICES=[('null',''),('درحال پیگیری','درحال پیگیری'),('انجام شده','انجام شده'),('انجام نشده','انجام نشده')]
    occupational_actions = models.CharField(choices=occupational_CHOICES,max_length=300,default='')
    occupational_disease_code = models.CharField(max_length=300)
    AST = models.IntegerField(default=0)
    AST_status = models.CharField(max_length=300)
    ALT = models.IntegerField(default=0)
    ALT_status = models.CharField(max_length=300)
    age_two = models.IntegerField(default=0)
    duration_of_employment = models.CharField(max_length=300)
    overweight = models.CharField(max_length=300)