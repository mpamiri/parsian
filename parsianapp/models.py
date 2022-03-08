from django.db import models
from django import forms
from django.conf import settings


class summary_of_results(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True,unique=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    start_month = models.IntegerField(default=1, null=True, blank=True)
    start_year = models.IntegerField(default=1300, null=True, blank=True)
    job = models.CharField(max_length=30, null=True, blank=True)
    examinations_code=models.CharField(max_length=20, null=True, blank=True)
    job_code = models.CharField( null=True, blank=True,max_length=30)
    gender_CHOICES = [('mard', 'مرد'), ('zan', 'زن')]
    gender = models.CharField(default='mard', choices=gender_CHOICES, null=True, blank=True, max_length=20)
    harmful_factors = models.CharField(max_length=100, null=True, blank=True)
    CODE_CHOICES = [(1, '1'), (2, '2'), (3, '3')]
    code = models.IntegerField(default=1, choices=CODE_CHOICES, null=True, blank=True)
    age = models.IntegerField(default=1300, null=True, blank=True)
    length = models.IntegerField(default=100, null=True, blank=True)
    weight = models.IntegerField(default=20, null=True, blank=True)
    body_mass = models.CharField(max_length=300, null=True, blank=True)
    body_mass_status = models.CharField(max_length=300, null=True, blank=True)
    blood_sugar = models.IntegerField(default=100, null=True, blank=True)
    blood_sugar_status = models.CharField(max_length=300, null=True, blank=True)
    blood_pressure = models.IntegerField(default=0, null=True, blank=True)
    blood_pressure_status = models.CharField(max_length=300, null=True, blank=True)
    cholesterol = models.IntegerField(default=0, null=True, blank=True)
    cholesterol_status = models.CharField(max_length=300, null=True, blank=True)
    triglyceride = models.IntegerField(default=0, null=True, blank=True)
    triglyceride_status = models.CharField(max_length=300, null=True, blank=True)
    URINE_CHOICES = [('null', ''), ('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('none', 'ندارد')]
    urine = models.CharField(choices=URINE_CHOICES, max_length=300, default='', null=True, blank=True)
    breathing_CHOICES = [('null', ''), ('normal', 'نرمال'), ('tahdidi', 'تحدیدی'), ('ensedadi', 'انسدادی'),
                         ('try', 'نیاز به تکرار'), ('namaie_toaman', 'نمای توامان تحدیدی وانسدادی'),
                         ('none', 'ندارد')]
    breathing_test = models.CharField(choices=breathing_CHOICES, max_length=300, default='null', null=True, blank=True)
    left_ear_CHOICES = [('null', ''), ('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'),
                        ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'),
                        ('kahesh_shenavai_nashi-az-seda', 'کاهش شنوایی ناشی از صدا'),
                        ('toaman_hedayati_va_hesi-asabi', 'توامان هدایتی و حسی عصبی'), ('none', 'ندارد')]
    left_ear_hearing = models.CharField(choices=left_ear_CHOICES, max_length=300, default='', null=True, blank=True)
    right_ear_CHOICES = [('null', ''), ('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'),
                        ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'),
                        ('kahesh_shenavai_nashi-az-seda', 'کاهش شنوایی ناشی از صدا'),
                        ('toaman_hedayati_va_hesi-asabi', 'توامان هدایتی و حسی عصبی'), ('none', 'ندارد')]
    right_ear_hearing = models.CharField(choices=right_ear_CHOICES, max_length=300, default='', null=True, blank=True)
    left_eye_vision = models.IntegerField(default=0, null=True, blank=True)
    left_eye_vision_status = models.CharField(max_length=300, null=True, blank=True)
    left_eye_vision_with_glasses = models.IntegerField(default=0, null=True, blank=True)
    right_eye_vision = models.IntegerField(default=0, null=True, blank=True)
    right_eye_vision_status = models.CharField(max_length=300, null=True, blank=True)
    right_eye_vision_with_glasses = models.IntegerField(default=0, null=True, blank=True)
    color_CHOICES = [('null', ''), ('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('tashkhis_rang_ghermez', 'تشخیص رنگ قرمز'),
                     ('none', 'ندارد')]
    color_vision = models.CharField(choices=color_CHOICES, max_length=300, default='', null=True, blank=True)
    field_CHOICES = [('null', ''), ('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('none', 'ندارد')]
    field_of_veiw = models.CharField(choices=field_CHOICES, max_length=300, default='', null=True, blank=True)
    depth_CHOICES = [('null', ''), ('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('none', 'ندارد')]
    depth_vision = models.CharField(choices=depth_CHOICES, max_length=300, default='', null=True, blank=True)
    breast_CHOICES = [('null', ''), ('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('none', 'ندارد')]
    breast_photo = models.CharField(choices=breast_CHOICES, max_length=300, default='', null=True, blank=True)
    heart_CHOICES = [('null', ''), ('normal', 'نرمال'), ('taghirat_gheir_ekhtesasi', 'تغییرات غیر اختصاصی'),
                     ('try', 'نیاز به تکرار'), ('not_normal', 'غیر نرمال'), ('none', 'ندارد')]
    heart = models.CharField(choices=heart_CHOICES, max_length=300, default='', null=True, blank=True)
    blood_lead = models.IntegerField(default=0, null=True, blank=True)
    blood_lead_status = models.CharField(max_length=300, null=True, blank=True)
    chratinin = models.IntegerField(default=0, null=True, blank=True)
    PSA = models.IntegerField(default=0, null=True, blank=True)
    PSA_status = models.CharField(max_length=300, null=True, blank=True)
    D3 = models.IntegerField(default=0, null=True, blank=True)
    TSH = models.IntegerField(default=0, null=True, blank=True)
    TSH_status = models.CharField(max_length=300, null=True, blank=True)
    problem = models.CharField(max_length=300, null=True, blank=True)
    problem_CHOICES = [('null', ''), ('darad', 'دارد'), ('none', 'ندارد')]
    problems_with_the_persons_job = models.CharField(choices=problem_CHOICES, max_length=300, default='', null=True,blank=True)
    recommendations = models.CharField(max_length=300, null=True, blank=True)
    refer_CHOICES = [('null', ''), ('none', 'ندارد'), ('ghalb_orogh', 'قلب و عروق'), ('dakheli', 'داخلی'), ('rie', 'ریه'),
                     ('ghodad', 'غدد'), ('saier', 'سایر')]
    refer_to_specialist = models.CharField(choices=refer_CHOICES, max_length=300, default='', null=True, blank=True)
    final_CHOICES = [('null', ''), ('belamane', 'بلامانع'), ('taghir_shekl', 'تغییر شغل'), ('mashrot', 'مشروط'),
                     ('comision', 'کمیسیون')]
    final_theory = models.CharField(choices=final_CHOICES, max_length=300, default='', null=True, blank=True)
    reson_for_opening_the_case = models.CharField(max_length=300, null=True, blank=True)
    occupational_CHOICES = [('null', ''), ('darhal_peygiri', 'درحال پیگیری'), ('done', 'انجام شده'),
                            ('not_done', 'انجام نشده')]
    occupational_actions = models.CharField(choices=occupational_CHOICES, max_length=300, default='', null=True,
                                            blank=True)
    occupational_disease_code = models.CharField(max_length=300, null=True, blank=True)
    AST = models.IntegerField(default=0, null=True, blank=True)
    AST_status = models.CharField(max_length=300, null=True, blank=True)
    ALT = models.IntegerField(default=0, null=True, blank=True)
    ALT_status = models.CharField(max_length=300, null=True, blank=True)
    age_two = models.IntegerField(default=0, null=True, blank=True)
    duration_of_employment = models.CharField(max_length=300, null=True, blank=True)
    overweight = models.CharField(max_length=300, null=True, blank=True)




class submit_company(models.Model):
    company = models.CharField(max_length=20, null=True, blank=True)
    doctor = models.CharField(max_length=20, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    specialist = models.CharField(max_length=20, null=True, blank=True)
    examinations_code=models.CharField(max_length=20, null=True, blank=True)


class disease(models.Model):
    examinations_code=models.CharField(max_length=20, null=True, blank=True)


