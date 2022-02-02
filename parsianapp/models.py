from django.db import models
from django import forms

class summary_of_results(models.Model):
    name = models.CharField(max_length=20)
    start_month = models.IntegerField(default=0)
    start_year = models.IntegerField(default=0)
    job = models.CharField(max_length=30)
    harmful_factors = models.CharField(max_length=100)
    CODE_CHOICES=[(1,'1'),(2,'2'),(3,'3')]
    code = models.IntegerField(default=0,choices=CODE_CHOICES)
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
    URINE_CHOICES=[(normal,'نرمال'),(not_normal,'غیر نرمال'),(none,'ندارد')]
    urine = models.CharField(choices=URINE_CHOICES)
    breathing_CHOICES=[(normal,'نرمال'),(tahdidi,'تحدیدی'),(ensedadi,'انسدادی'),(niaz_be_tekrar,'نیاز به تکرار'),(namaie_toaman,'نمای توامان تحدیدی وانسدادی'),(none,'ندارد')]
    breathing_test = models.CharField(choices=breathing_CHOICES)
    left_ear_CHOICES=[('نرمال'),('کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی'),('ندارد')]
    left_ear_hearing = models.CharField(choices=breathing_CHOICES)
    right_ear_CHOICES=[('نرمال'),('کاهش شنوایی هدایتی'),('کاهش شنوایی حسی عصبی'),('کاهش شنوایی ناشی از صدا'),('توامان هدایتی و حسی عصبی'),('ندارد')]
    right_ear_hearing = models.CharField(choices=breathing_CHOICES)
    left_eye_vision = models.IntegerField(default=0)
    left_eye_vision_status = models.CharField(max_length=300)
    left_eye_vision_with_glasses = models.IntegerField(default=0)
    right_eye_vision = models.IntegerField(default=0)
    right_eye_vision_status = models.CharField(max_length=300)
    right_eye_vision_with_glasses = models.IntegerField(default=0)
    CODE_CHOICES=[('نرمال'),('غیر نرمال'),('تشخیص رنگ قرمز'),('ندارد')]
    color_vision = models.CharField(choices=breathing_CHOICES)
    CODE_CHOICES=[('نرمال'),('غیر نرمال'),('ندارد')]
    field_of_veiw = models.CharField(choices=breathing_CHOICES)
    CODE_CHOICES=[('نرمال'),('غیر نرمال'),('ندارد')]
    depth_vision = models.CharField(choices=breathing_CHOICES)
    CODE_CHOICES=[('نرمال'),('غیر نرمال'),('ندارد')]
    breast_photo = models.CharField(choices=breathing_CHOICES)
    CODE_CHOICES=[('نرمال'),('تغییرات غیر اختصاصی'),('نیاز به تکرار'),('غیر نرمال'),('ندارد')]
    blood_lead = models.CharField(choices=breathing_CHOICES)
    blood_lead_status = models.CharField(max_length=300)
    PSA = models.IntegerField(default=0)
    PSA_status = models.CharField(max_length=300)
    TSH = models.IntegerField(default=0)
    TSH_status = models.CharField(max_length=300)
    problem = models.CharField(max_length=300)
    CODE_CHOICES=[('دارد'),('ندارد')]
    problems_with_the_persons_job = models.CharField(choices=breathing_CHOICES)
    recommendations = models.CharField(max_length=300)
    CODE_CHOICES=[('ندارد'),('قلب و عروق'),('داخلی'),('ریه'),('غدد'),('سایر')]
    refer_to_specialist = models.CharField(choices=breathing_CHOICES)
    CODE_CHOICES=[('بلامانع'),('تغییر شغل'),('مشروط'),('کمیسیون')]
    final_theory = models.CharField(choices=breathing_CHOICES)
    reson_for_opening_the_case = models.CharField(max_length=300)
    CODE_CHOICES=[('درحال پیگیری'),('انجام شده'),('انجام نشده')]
    occupational_actions = models.CharField(choices=breathing_CHOICES)
    occupational_disease_code = models.CharField(max_length=300)
    AST = models.IntegerField(default=0)
    AST_status = models.CharField(max_length=300)
    ALT = models.IntegerField(default=0)
    ALT_status = models.CharField(max_length=300)
    age_two = models.IntegerField(default=0)
    duration_of_employment = models.CharField(max_length=300)
    overweight = models.CharField(max_length=300)