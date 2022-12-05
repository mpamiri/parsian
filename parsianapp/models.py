from django.db import models
from django import forms
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import timezone
from django.core.exceptions import NON_FIELD_ERRORS

class Company(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True,unique=True)

    def __str__(self):
        return f'{self.name}'

class ExaminationsCourse(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True)
    year = models.IntegerField(null=True, blank=True)
    specialist = models.CharField(max_length=250, null=True, blank=True)
    doctor = models.CharField(max_length=250, null=True, blank=True)
    examinations_code = models.CharField(max_length=250, null=True, blank=True,unique=True)
    def __str__(self):
        return f'{self.examinations_code}'


class Disease_Model(models.Model):
    examinations_code=models.CharField(max_length=250, null=True, blank=True)
    p_examinations_code=models.CharField(max_length=250, null=True, blank=True)
    p_name = models.CharField(max_length=250,null=True,blank=True)
    p_personal_code = models.IntegerField(null=True,blank=True)
    p_fathers_name = models.CharField(max_length=250, null=True, blank=True)
    p_age = models.IntegerField(null=True,blank=True)
    e_examinations_code=models.CharField(max_length=250, null=True, blank=True)
    e_name = models.CharField(max_length=250,null=True,blank=True)
    e_personal_code = models.IntegerField(null=True,blank=True)
    e_fathers_name = models.CharField(max_length=250, null=True, blank=True)
    e_age = models.IntegerField(null=True,blank=True)
    order_CHOICES = [(1, '1'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50')]
    order_number = models.IntegerField(default=1, choices=order_CHOICES, null=True,blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    personal_code = models.IntegerField(null=True,blank=True)
    fathers_name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)
    


class Personal_Species_Model(models.Model):
    examinations_code = models.ForeignKey(ExaminationsCourse, on_delete=models.CASCADE,blank=True)
    user = models.CharField(max_length=250, null=True, blank=True)
    examinations_type_CHOICES = [('badv_estekhdam', 'بدو استخدام'), ('dore_e', 'دوره ای'), ('bazgasht_be_kar', 'بازگشت به کار')]
    examinations_type = models.CharField(choices=examinations_type_CHOICES, max_length=250,blank=True,null=True)
    species_date_year=models.IntegerField( null=True, blank=True)
    species_date_month=models.IntegerField(null=True, blank=True)
    species_date_day=models.IntegerField(null=True, blank=True)
    profil_number=models.IntegerField(null=True, blank=True)
    employment_number=models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250,default=None, null=True, blank=True)
    fathers_name = models.CharField(max_length=250, null=True, blank=True)
    gender_CHOICES = [('mard', 'مرد'), ('zan', 'زن')]
    gender = models.CharField(default='mard', choices=gender_CHOICES, max_length=250, null=True, blank=True)
    marriage_status_CHOICES = [('mojarad', 'مجرد'), ('motahel', 'متاهل')]
    marriage_status = models.CharField(default='mojarad', choices=marriage_status_CHOICES,  max_length=250, null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(default=None, null=True, blank=True)
    personal_code = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(1), MaxValueValidator(100)])
    military_status_CHOICES = [('khedmat_karde', 'خدمت کرده'), ('moaf', 'معاف'), ('khedmat_nakarde', 'خدمت نکرده')]
    military_status = models.CharField(default='khedmat_karde', choices=military_status_CHOICES, max_length=250, null=True, blank=True)
    raste = models.CharField(max_length=250, null=True, blank=True)
    medical_exemption_CHOICES = [('none', 'ندارد'),('pezeshki', 'پزشکی'), ('not_pezeshki', 'غیر پزشکی')]
    medical_exemption = models.CharField(default='none', choices=medical_exemption_CHOICES, max_length=250, null=True, blank=True)
    medical_exemption_reason = models.CharField(max_length=250, null=True, blank=True)
    job_name = models.CharField(max_length=250, null=True, blank=True)
    employer_name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)


    
class Job_History_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='history',null=True,blank=True)
    current_job = models.CharField(max_length=250, null=True, blank=True)
    current_job_duty = models.CharField(max_length=250, null=True, blank=True)
    current_job_from_year = models.IntegerField(null=True, blank=True)
    current_job_from_month = models.IntegerField(null=True, blank=True)
    current_job_to_year = models.IntegerField(null=True, blank=True)
    current_job_to_month = models.IntegerField(null=True, blank=True)
    durations = models.IntegerField(null=True, blank=True)
    # assessment = models.ForeignKey(Assessment_Model, on_delete=models.CASECADE)

class Assessment_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='assessment',null=True,blank=True)
    current_ph_noise = models.BooleanField(default=False)
    current_ph_erteash = models.BooleanField(default=False)
    current_ph_not_unizan = models.BooleanField(default=False)
    current_ph_unizan = models.BooleanField(default=False)
    current_ph_stress = models.BooleanField(default=False)
    current_ph_other = models.BooleanField(default=False)
    current_sh_dust = models.BooleanField(default=False)
    current_sh_metals = models.BooleanField(default=False)
    current_sh_halal = models.BooleanField(default=False)
    current_sh_afat = models.BooleanField(default=False)
    current_sh_asidvbaz = models.BooleanField(default=False)
    current_sh_gaz = models.BooleanField(default=False)
    current_bio_gazesh = models.BooleanField(default=False)
    current_bio_bactery = models.BooleanField(default=False)
    current_bio_virus = models.BooleanField(default=False)
    current_bio_angal = models.BooleanField(default=False)
    current_bio_other = models.BooleanField(default=False)
    current_er_standvsit = models.BooleanField(default=False)
    current_er_loop = models.BooleanField(default=False)
    current_er_hamlvnaghl = models.BooleanField(default=False)
    current_er_vaziat_namonaseb = models.BooleanField(default=False)
    current_er_other = models.BooleanField(default=False)
    current_rav_order = models.BooleanField(default=False)
    current_rav_stressor = models.BooleanField(default=False)
    current_rav_other = models.BooleanField(default=False)
    previous_ph_noise = models.BooleanField(default=False)
    previous_ph_erteash = models.BooleanField(default=False)
    previous_ph_not_unizan = models.BooleanField(default=False)
    previous_ph_unizan = models.BooleanField(default=False)
    previous_ph_stress = models.BooleanField(default=False)
    previous_ph_other = models.BooleanField(default=False)
    previous_sh_dust = models.BooleanField(default=False)
    previous_sh_metals = models.BooleanField(default=False)
    previous_sh_halal = models.BooleanField(default=False)
    previous_sh_afat = models.BooleanField(default=False)
    previous_sh_asidvbaz = models.BooleanField(default=False)
    previous_sh_gaz = models.BooleanField(default=False)
    previous_bio_gazesh = models.BooleanField(default=False)
    previous_bio_bactery = models.BooleanField(default=False)
    previous_bio_virus = models.BooleanField(default=False)
    previous_bio_angal = models.BooleanField(default=False)
    previous_bio_other = models.BooleanField(default=False)
    previous_er_standvsit = models.BooleanField(default=False)
    previous_er_loop = models.BooleanField(default=False)
    previous_er_hamlvnaghl = models.BooleanField(default=False)
    previous_er_vaziat_namonaseb = models.BooleanField(default=False)
    previous_er_other = models.BooleanField(default=False)
    previous_rav_order = models.BooleanField(default=False)
    previous_rav_stressor = models.BooleanField(default=False)
    previous_rav_other = models.BooleanField(default=False)   
    required_description = models.CharField(max_length=250, null=True, blank=True)
    kar_shenas = models.CharField(max_length=250, null=True, blank=True)
    kar_shenas_name = models.CharField(max_length=250, null=True, blank=True)
    ass_date_year=models.IntegerField(null=True, blank=True)
    ass_date_month=models.IntegerField(null=True, blank=True)
    ass_date_day=models.IntegerField(null=True, blank=True)
    assessments = models.CharField(max_length=250, null=True, blank=True)

class Personal_History_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='personalhistory',null=True,blank=True)    
    first_y = models.BooleanField(default=False)  
    first_n = models.BooleanField(default=False) 
    first_des = models.CharField(max_length=250, null=True, blank=True)
    second_y = models.BooleanField(default=False)  
    second_n = models.BooleanField(default=False) 
    second_des = models.CharField(max_length=250, null=True, blank=True)
    third_y = models.BooleanField(default=False)  
    third_n = models.BooleanField(default=False) 
    third_des = models.CharField(max_length=250, null=True, blank=True)
    fourth_y = models.BooleanField(default=False)  
    fourth_n = models.BooleanField(default=False) 
    fourth_des = models.CharField(max_length=250, null=True, blank=True)
    fifth_y = models.BooleanField(default=False)  
    fifth_n = models.BooleanField(default=False) 
    fifth_des = models.CharField(max_length=250, null=True, blank=True)
    sixth_y = models.BooleanField(default=False)  
    sixth_n = models.BooleanField(default=False) 
    sixth_des = models.CharField(max_length=250, null=True, blank=True)
    seventh_y = models.BooleanField(default=False)  
    seventh_n = models.BooleanField(default=False) 
    seventh_des = models.CharField(max_length=250, null=True, blank=True)
    eighth_y = models.BooleanField(default=False)  
    eighth_n = models.BooleanField(default=False) 
    eighth_des = models.CharField(max_length=250, null=True, blank=True)
    ninth_y = models.BooleanField(default=False)  
    ninth_n = models.BooleanField(default=False) 
    ninth_des = models.CharField(max_length=250, null=True, blank=True)
    tenth_y = models.BooleanField(default=False)  
    tenth_n = models.BooleanField(default=False) 
    tenth_des_number = models.IntegerField(null=True, blank=True)
    tenth_des_duration = models.CharField(max_length=250, null=True, blank=True)
    eleventh_y = models.BooleanField(default=False)  
    eleventh_n = models.BooleanField(default=False) 
    eleventh_des_number = models.IntegerField(null=True, blank=True)
    eleventh_des_duration = models.CharField(max_length=250, null=True, blank=True)
    twelfth_y = models.BooleanField(default=False)  
    twelfth_n = models.BooleanField(default=False) 
    twelfth_des = models.CharField(max_length=250, null=True, blank=True)
    thirteenth_y = models.BooleanField(default=False)  
    thirteenth_n = models.BooleanField(default=False) 
    thirteenth_des_type = models.CharField(max_length=250, null=True, blank=True)
    thirteenth_des_reason = models.CharField(max_length=250, null=True, blank=True)
    fourteenth_y = models.BooleanField(default=False)  
    fourteenth_n = models.BooleanField(default=False) 
    fourteenth_des = models.CharField(max_length=250, null=True, blank=True)
    fifteenth_y = models.BooleanField(default=False)  
    fifteenth_n = models.BooleanField(default=False) 
    fifteenth_des = models.CharField(max_length=250, null=True, blank=True)
    sixteenth_y = models.BooleanField(default=False)  
    sixteenth_n = models.BooleanField(default=False) 
    sixteenth_des = models.CharField(max_length=250, null=True, blank=True)
    

class Examinations_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='examinations',null=True,blank=True) 
    exa_date_year=models.IntegerField(null=True, blank=True)
    exa_date_month=models.IntegerField(null=True, blank=True)
    exa_date_day=models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    blood_pressure = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    local_sym_kahesh_vazn = models.BooleanField(default=False)
    local_sym_kahesh_eshteha = models.BooleanField(default=False)
    local_sym_khastegi = models.BooleanField(default=False)
    local_sym_ekhtelal_dar_khab = models.BooleanField(default=False)
    local_sym_tarigh = models.BooleanField(default=False)
    local_sym_adam_tahamol = models.BooleanField(default=False)
    local_sym_tab = models.BooleanField(default=False)
    local_sym_other = models.BooleanField(default=False)
    local_sym_without_sign = models.BooleanField(default=False)
    local_sign_zaheri = models.BooleanField(default=False)
    local_sign_rang_paride = models.BooleanField(default=False)
    local_sign_other = models.BooleanField(default=False)
    local_sign_without_sign = models.BooleanField(default=False)
    local_des = models.CharField(max_length=250, null=True, blank=True)
    
    eye_sym_kahesh_binayi = models.BooleanField(default=False)
    eye_sym_tari_did = models.BooleanField(default=False)
    eye_sym_khastegi = models.BooleanField(default=False)
    eye_sym_dobini = models.BooleanField(default=False)
    eye_sym_sozesh = models.BooleanField(default=False)
    eye_sym_tars_az_nor = models.BooleanField(default=False)
    eye_sym_ashk = models.BooleanField(default=False)
    eye_sym_other = models.BooleanField(default=False)
    eye_sym_without_sign = models.BooleanField(default=False)
    eye_sign_reflex = models.BooleanField(default=False)
    eye_sign_red = models.BooleanField(default=False)
    eye_sign_sklrai = models.BooleanField(default=False)
    eye_sign_nistagemos = models.BooleanField(default=False)
    eye_sign_other = models.BooleanField(default=False)
    eye_sign_without_sign = models.BooleanField(default=False)
    eye_des = models.CharField(max_length=250, null=True, blank=True)

    skin_sym_kharesh_post = models.BooleanField(default=False)
    skin_sym_rizesh_mo = models.BooleanField(default=False)
    skin_sym_red = models.BooleanField(default=False)
    skin_sym_taghir_post = models.BooleanField(default=False)
    skin_sym_zakhm = models.BooleanField(default=False)
    skin_sym_poste_rizi = models.BooleanField(default=False)
    skin_sym_taghir_nakhon = models.BooleanField(default=False)
    skin_sym_other = models.BooleanField(default=False)
    skin_sym_without_sign = models.BooleanField(default=False)
    skin_sign_makol = models.BooleanField(default=False)
    skin_sign_papol = models.BooleanField(default=False)
    skin_sign_nadol = models.BooleanField(default=False)
    skin_sign_vezikol = models.BooleanField(default=False)
    skin_sign_zakhm = models.BooleanField(default=False)
    skin_sign_kahir = models.BooleanField(default=False)
    skin_sign_klabing = models.BooleanField(default=False)
    skin_sign_rizesh_mantaghe = models.BooleanField(default=False)
    skin_sign_rizesh_general = models.BooleanField(default=False)
    skin_sign_taghirat_peygmani = models.BooleanField(default=False)
    skin_sign_other = models.BooleanField(default=False)
    skin_sign_without_sign = models.BooleanField(default=False)
    skin_des = models.CharField(max_length=250, null=True, blank=True)

    gosh_sym_kahesh_shenavaii = models.BooleanField(default=False)
    gosh_sym_vez_vez_gosh = models.BooleanField(default=False)
    gosh_sym_sargije = models.BooleanField(default=False)
    gosh_sym_dard_gosh = models.BooleanField(default=False)
    gosh_sym_tarashoh_gosh = models.BooleanField(default=False)
    gosh_sym_gereftegi_seda = models.BooleanField(default=False)
    gosh_sym_galodard = models.BooleanField(default=False)
    gosh_sym_abrrizesh_bini = models.BooleanField(default=False)
    gosh_sym_ekhtelal_boyayi = models.BooleanField(default=False)
    gosh_sym_khareshvsozesh = models.BooleanField(default=False)
    gosh_sym_khonrizi = models.BooleanField(default=False)
    gosh_sym_khoshki = models.BooleanField(default=False)
    gosh_sym_ehsas = models.BooleanField(default=False)
    gosh_sym_other = models.BooleanField(default=False)
    gosh_sym_without_sign = models.BooleanField(default=False)
    gosh_sign_eltehab_parde = models.BooleanField(default=False)
    gosh_sign_paregi = models.BooleanField(default=False)
    gosh_sign_afzayesh = models.BooleanField(default=False)
    gosh_sign_tarashoh = models.BooleanField(default=False)
    gosh_sign_egzodai = models.BooleanField(default=False)
    gosh_sign_red = models.BooleanField(default=False)
    gosh_sign_polip = models.BooleanField(default=False)
    gosh_sign_tndrs = models.BooleanField(default=False)
    gosh_sign_lead = models.BooleanField(default=False)
    gosh_sign_bad_smell = models.BooleanField(default=False)
    gosh_sign_eltehab_lase = models.BooleanField(default=False)
    gosh_sign_zakhm = models.BooleanField(default=False)
    gosh_sign_other = models.BooleanField(default=False)
    gosh_sign_without_sign = models.BooleanField(default=False)
    gosh_des = models.CharField(max_length=250, null=True, blank=True)

    sar_sym_dard_gardan = models.BooleanField(default=False)
    sar_sym_tode_gardani = models.BooleanField(default=False)
    sar_sym_other = models.BooleanField(default=False)
    sar_sym_without_sign = models.BooleanField(default=False)
    sar_sign_bozorgi_tiroid = models.BooleanField(default=False)
    sar_sign_gardani = models.BooleanField(default=False)
    sar_sign_other = models.BooleanField(default=False)
    sar_sign_without_sign = models.BooleanField(default=False)
    sar_des = models.CharField(max_length=250, null=True, blank=True)

    rie_sym_sorfe = models.BooleanField(default=False)
    rie_sym_khelt = models.BooleanField(default=False)
    rie_sym_tangi = models.BooleanField(default=False)
    rie_sym_sine = models.BooleanField(default=False)
    rie_sym_other = models.BooleanField(default=False)
    rie_sym_without_sign = models.BooleanField(default=False)
    rie_sign_zaheri = models.BooleanField(default=False)
    rie_sign_khoshonat = models.BooleanField(default=False)
    rie_sign_vizing = models.BooleanField(default=False)
    rie_sign_cracel = models.BooleanField(default=False)
    rie_sign_taki_pene = models.BooleanField(default=False)
    rie_sign_kahesh_sedaha = models.BooleanField(default=False)
    rie_sign_other = models.BooleanField(default=False)
    rie_sign_without_sign = models.BooleanField(default=False)
    rie_des = models.CharField(max_length=250, null=True, blank=True)

    ghalb_sym_dard = models.BooleanField(default=False)
    ghalb_sym_tapesh = models.BooleanField(default=False)
    ghalb_sym_tangi_shabane = models.BooleanField(default=False)
    ghalb_sym_tangi_khabide = models.BooleanField(default=False)
    ghalb_sym_sianoz = models.BooleanField(default=False)
    ghalb_sym_senkop = models.BooleanField(default=False)
    ghalb_sym_other = models.BooleanField(default=False)
    ghalb_sym_without_sign = models.BooleanField(default=False)
    ghalb_sign_s = models.BooleanField(default=False)
    ghalb_sign_seda_ezafe = models.BooleanField(default=False)
    ghalb_sign_aritmi = models.BooleanField(default=False)
    ghalb_sign_varis_tahtani = models.BooleanField(default=False)
    ghalb_sign_varis_foghani = models.BooleanField(default=False)
    ghalb_sign_andam = models.BooleanField(default=False)
    ghalb_sign_other = models.BooleanField(default=False)
    ghalb_sign_without_sign = models.BooleanField(default=False)
    ghalb_des = models.CharField(max_length=250, null=True, blank=True)

    shekam_sym_bi_eshteha = models.BooleanField(default=False)
    shekam_sym_tahavo = models.BooleanField(default=False)
    shekam_sym_estefragh = models.BooleanField(default=False)
    shekam_sym_dard_shekam = models.BooleanField(default=False)
    shekam_sym_soozesh = models.BooleanField(default=False)
    shekam_sym_eshal = models.BooleanField(default=False)
    shekam_sym_yobosat = models.BooleanField(default=False)
    shekam_sym_ghiri = models.BooleanField(default=False)
    shekam_sym_roshan = models.BooleanField(default=False)
    shekam_sym_ekhtelal = models.BooleanField(default=False)
    shekam_sym_other = models.BooleanField(default=False)
    shekam_sym_without_sign = models.BooleanField(default=False)
    shekam_sign_shekami = models.BooleanField(default=False)
    shekam_sign_rebond = models.BooleanField(default=False)
    shekam_sign_hepatomegaly = models.BooleanField(default=False)
    shekam_sign_espelnomegali = models.BooleanField(default=False)
    shekam_sign_asib = models.BooleanField(default=False)
    shekam_sign_tode_shekami = models.BooleanField(default=False)
    shekam_sign_distansion = models.BooleanField(default=False)
    shekam_sign_other = models.BooleanField(default=False)
    shekam_sign_without_sign = models.BooleanField(default=False)
    shekam_des = models.CharField(max_length=250, null=True, blank=True)

    colie_sym_soozesh = models.BooleanField(default=False)
    colie_sym_tekrar = models.BooleanField(default=False)
    colie_sym_khoni = models.BooleanField(default=False)
    colie_sym_pahlo = models.BooleanField(default=False)
    colie_sym_sangini = models.BooleanField(default=False)
    colie_sym_other = models.BooleanField(default=False)
    colie_sym_without_sign = models.BooleanField(default=False)
    colie_sign_cva = models.BooleanField(default=False)
    colie_sign_varikosel = models.BooleanField(default=False)
    colie_sign_other = models.BooleanField(default=False)
    colie_sign_without_sign = models.BooleanField(default=False)
    colie_des = models.CharField(max_length=250, null=True, blank=True)

    eskelety_sym_mafsal = models.BooleanField(default=False)
    eskelety_sym_kamar_dard = models.BooleanField(default=False)
    eskelety_sym_zano = models.BooleanField(default=False)
    eskelety_sym_shane = models.BooleanField(default=False)
    eskelety_sym_other_mafasel = models.BooleanField(default=False)
    eskelety_sym_other = models.BooleanField(default=False)
    eskelety_sym_without_sign = models.BooleanField(default=False)
    eskelety_sign_mahdodiat = models.BooleanField(default=False)
    eskelety_sign_kahesh_foghani = models.BooleanField(default=False)
    eskelety_sign_kahesh_tahtani = models.BooleanField(default=False)
    eskelety_sign_eskolioz = models.BooleanField(default=False)
    eskelety_sign_empotasion = models.BooleanField(default=False)
    eskelety_sign_slr = models.BooleanField(default=False)
    eskelety_sign_r_slr = models.BooleanField(default=False)
    eskelety_sign_other = models.BooleanField(default=False)
    eskelety_sign_without_sign = models.BooleanField(default=False)
    eskelety_des = models.CharField(max_length=250, null=True, blank=True)

    asabi_sym_sar_dard = models.BooleanField(default=False)
    asabi_sym_giji = models.BooleanField(default=False)
    asabi_sym_larzesh = models.BooleanField(default=False)
    asabi_sym_ekhtelal = models.BooleanField(default=False)
    asabi_sym_tashanoj = models.BooleanField(default=False)
    asabi_sym_gez_gez = models.BooleanField(default=False)
    asabi_sym_other = models.BooleanField(default=False)
    asabi_sym_without_sign = models.BooleanField(default=False)
    asabi_sign_tabi_e = models.BooleanField(default=False)
    asabi_sign_gheir_tabi_e = models.BooleanField(default=False)
    asabi_sign_mokhtal = models.BooleanField(default=False)
    asabi_sign_trmor = models.BooleanField(default=False)
    asabi_sign_hesi = models.BooleanField(default=False)
    asabi_sign_tinel = models.BooleanField(default=False)
    asabi_sign_falen = models.BooleanField(default=False)
    asabi_sign_other = models.BooleanField(default=False)
    asabi_sign_without_sign = models.BooleanField(default=False)
    asabi_des = models.CharField(max_length=250, null=True, blank=True)

    ravan_sym_asabaniat = models.BooleanField(default=False)
    ravan_sym_parkhashgari = models.BooleanField(default=False)
    ravan_sym_ezterab = models.BooleanField(default=False)
    ravan_sym_kholgh = models.BooleanField(default=False)
    ravan_sym_angize = models.BooleanField(default=False)
    ravan_sym_other = models.BooleanField(default=False)
    ravan_sym_without_sign = models.BooleanField(default=False)
    ravan_sign_hazyan = models.BooleanField(default=False)
    ravan_sign_tavahom = models.BooleanField(default=False)
    ravan_sign_oriantasion = models.BooleanField(default=False)
    ravan_sign_other = models.BooleanField(default=False)
    ravan_sign_without_sign = models.BooleanField(default=False)
    ravan_des = models.CharField(max_length=250, null=True, blank=True)

    other = models.CharField(max_length=250, null=True, blank=True)
    body_mass = models.IntegerField(null=True, blank=True)
    code = models.CharField(default=None, null=True, blank=True,max_length=250)
    not_normals = models.CharField(max_length=250,null=True,blank=True)

class Experiments_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='experiment',null=True,blank=True) 
    exp_date_year=models.IntegerField(null=True, blank=True)
    exp_date_month=models.IntegerField(null=True, blank=True)
    exp_date_day=models.IntegerField(null=True, blank=True)
    cbc_wbc=models.IntegerField(null=True, blank=True)
    cbc_rbc=models.IntegerField(null=True, blank=True)
    cbc_hb=models.IntegerField(null=True, blank=True)
    cbc_htc=models.IntegerField(null=True, blank=True)
    cbc_plt=models.IntegerField(null=True, blank=True)
    ua_prot=models.IntegerField(null=True, blank=True)
    ua_glu=models.IntegerField(null=True, blank=True)
    ua_rbc=models.IntegerField(null=True, blank=True)
    ua_wbc=models.IntegerField(null=True, blank=True)
    ua_bact=models.IntegerField(null=True, blank=True)
    fbs=models.IntegerField(null=True, blank=True)
    chol=models.IntegerField(null=True, blank=True)
    ldl=models.IntegerField(null=True, blank=True)
    hdl=models.IntegerField(null=True, blank=True)
    tg=models.IntegerField(null=True, blank=True)
    psa=models.IntegerField(null=True, blank=True)
    cr=models.IntegerField(null=True, blank=True)
    alt=models.IntegerField(null=True, blank=True)
    ast=models.IntegerField(null=True, blank=True)
    alk=models.IntegerField(null=True, blank=True)
    lead=models.IntegerField(null=True, blank=True)
    d=models.IntegerField(null=True, blank=True)
    tsh=models.IntegerField(null=True, blank=True)
    cbc_wbc_status=models.BooleanField(default=True)
    cbc_rbc_status=models.BooleanField(default=True)
    cbc_hb_status=models.BooleanField(default=True)
    cbc_htc_status=models.BooleanField(default=True)
    cbc_plt_status=models.BooleanField(default=True)
    ua_prot_status=models.BooleanField(default=True)
    ua_glu_status=models.BooleanField(default=True)
    ua_rbc_status=models.BooleanField(default=True)
    ua_wbc_status=models.BooleanField(default=True)
    ua_bact_status=models.BooleanField(default=True)
    fbs_status=models.BooleanField(default=True)
    chol_status=models.BooleanField(default=True)
    ldl_status=models.BooleanField(default=True)
    hdl_status=models.BooleanField(default=True)
    tg_status=models.BooleanField(default=True)
    psa_status=models.BooleanField(default=True)
    cr_status=models.BooleanField(default=True)
    alt_status=models.BooleanField(default=True)
    ast_status=models.BooleanField(default=True)
    alk_status=models.BooleanField(default=True)
    lead_status=models.BooleanField(default=True)
    se_status_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    se_status = models.CharField(default=None, choices=se_status_CHOICES, null=True, blank=True,max_length=10)
    ppd_status_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    ppd_status = models.CharField(default=None, choices=ppd_status_CHOICES, null=True, blank=True,max_length=10)
    d_status=models.BooleanField(default=True)
    tsh_status=models.BooleanField(default=True)
    first_type= models.CharField(max_length=250, null=True, blank=True)
    first_result= models.CharField(max_length=250, null=True, blank=True)
    first_date_year=models.IntegerField(null=True, blank=True)
    first_date_month=models.IntegerField(null=True, blank=True)
    first_date_day=models.IntegerField(null=True, blank=True)
    second_type= models.CharField(max_length=250, null=True, blank=True)
    second_result= models.CharField(max_length=250, null=True, blank=True)
    second_date_year=models.IntegerField(null=True, blank=True)
    second_date_month=models.IntegerField(null=True, blank=True)
    second_date_day=models.IntegerField(null=True, blank=True)
    third_type= models.CharField(max_length=250, null=True, blank=True)
    third_result= models.CharField(max_length=250, null=True, blank=True)
    third_date_year=models.IntegerField(null=True, blank=True)
    third_date_month=models.IntegerField(null=True, blank=True)
    third_date_day=models.IntegerField(null=True, blank=True)


class Para_Clinic_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='para',null=True,blank=True) 
    opto_date_year=models.IntegerField(null=True, blank=True)
    opto_date_month=models.IntegerField(null=True, blank=True)
    opto_date_day=models.IntegerField(null=True, blank=True)
    opto_hedat_r_ba=models.IntegerField(null=True, blank=True)
    opto_hedat_r_bi=models.IntegerField(null=True, blank=True)
    hedat_r_status_CHOICES = [('adam_did', 'عدم دید'), ('fc', 'FC'), ('daraie_did', 'دارای دید')]
    opto_hedat_r_status=models.CharField(null=True, blank=True,max_length=250,choices=hedat_r_status_CHOICES) 
    opto_hedat_l_ba=models.IntegerField(null=True, blank=True)
    opto_hedat_l_bi=models.IntegerField(null=True, blank=True)
    hedat_l_status_CHOICES = [('adam_did', 'عدم دید'), ('fc', 'FC'), ('daraie_did', 'دارای دید')]
    opto_hedat_l_status=models.CharField(null=True, blank=True,max_length=250,choices=hedat_l_status_CHOICES) 
    rangi_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    opto_rangi=models.CharField(null=True, blank=True,max_length=250,choices=rangi_CHOICES)
    meidan_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    opto_meidan=models.CharField(null=True, blank=True,max_length=250,choices=meidan_CHOICES)
    opto_omgh = models.IntegerField(null=True, blank=True)
    opto_r_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    opto_r=models.CharField(null=True, blank=True,max_length=250,choices=opto_r_CHOICES)
    opto_l_CHOICES = [('normal', 'نرمال'), ('not_normal', 'غیر نرمال')]
    opto_l=models.CharField(null=True, blank=True,max_length=250,choices=opto_l_CHOICES)


    audio_date_year=models.IntegerField(null=True, blank=True)
    audio_date_month=models.IntegerField(null=True, blank=True)
    audio_date_day=models.IntegerField(null=True, blank=True)
    audio_r_status_CHOICES = [('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'), ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'), ('kahesh_shenavai_nashi_az_seda', 'کاهش شنوایی ناشی از صدا'), ('toaman_hedayati_va_hesi_asabi', 'توامان هدایتی و حسی عصبی')]
    audio_r_tafsir = models.CharField(max_length=250,choices=audio_r_status_CHOICES, null=True, blank=True)
    audio_l_status_CHOICES = [('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'), ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'), ('kahesh_shenavai_nashi_az_seda', 'کاهش شنوایی ناشی از صدا'), ('toaman_hedayati_va_hesi_asabi', 'توامان هدایتی و حسی عصبی')]
    audio_l_tafsir = models.CharField(max_length=250,choices=audio_l_status_CHOICES, null=True, blank=True)
    audio_r_eight_ac = models.IntegerField(null=True, blank=True)
    audio_r_eight_bc = models.IntegerField(null=True, blank=True)
    audio_r_six_ac = models.IntegerField(null=True, blank=True)
    audio_r_six_bc = models.IntegerField(null=True, blank=True)
    audio_r_four_ac = models.IntegerField(null=True, blank=True)
    audio_r_four_bc = models.IntegerField(null=True, blank=True)
    audio_r_three_ac = models.IntegerField(null=True, blank=True)
    audio_r_three_bc = models.IntegerField(null=True, blank=True)
    audio_r_two_ac = models.IntegerField(null=True, blank=True)
    audio_r_two_bc = models.IntegerField(null=True, blank=True)
    audio_r_one_ac = models.IntegerField(null=True, blank=True)
    audio_r_one_bc = models.IntegerField(null=True, blank=True)
    audio_r_five_ac = models.IntegerField(null=True, blank=True)
    audio_r_five_bc = models.IntegerField(null=True, blank=True)
    audio_l_eight_ac = models.IntegerField(null=True, blank=True)
    audio_l_eight_bc = models.IntegerField(null=True, blank=True)
    audio_l_six_ac = models.IntegerField(null=True, blank=True)
    audio_l_six_bc = models.IntegerField(null=True, blank=True)
    audio_l_four_ac = models.IntegerField(null=True, blank=True)
    audio_l_four_bc = models.IntegerField(null=True, blank=True)
    audio_l_three_ac = models.IntegerField(null=True, blank=True)
    audio_l_three_bc = models.IntegerField(null=True, blank=True)
    audio_l_two_ac = models.IntegerField(null=True, blank=True)
    audio_l_two_bc = models.IntegerField(null=True, blank=True)
    audio_l_one_ac = models.IntegerField(null=True, blank=True)
    audio_l_one_bc = models.IntegerField(null=True, blank=True)
    audio_l_five_ac = models.IntegerField(null=True, blank=True)
    audio_l_five_bc = models.IntegerField(null=True, blank=True)

    espiro_date_year=models.IntegerField(null=True, blank=True)
    espiro_date_month=models.IntegerField(null=True, blank=True)
    espiro_date_day=models.IntegerField(null=True, blank=True)
    espiro_fevvfvc = models.CharField(max_length=250, null=True, blank=True)
    espiro_fev = models.CharField(max_length=250, null=True, blank=True)
    espiro_fvc = models.CharField(max_length=250, null=True, blank=True)
    espiro_vext = models.CharField(max_length=250, null=True, blank=True)
    espiro_pef = models.CharField(max_length=250, null=True, blank=True)
    espiro_fef = models.CharField(max_length=250, null=True, blank=True)
    ESPIRO_TAFSIR_CHOICES = [('normal', 'نرمال'), ('ensedadi', 'انسدادی'), ('tahdidi', 'تحدیدی'),('ensedadivtahdidi','انسدادی و تحدیدی'),('again','نیاز به تکرار')]
    espiro_tafsir = models.CharField(max_length=250,choices=ESPIRO_TAFSIR_CHOICES, null=True, blank=True)

    cxr_CHOICES = [('normal', 'نرمال'),('not_normal','غیر نرمال')]
    other_cxr = models.CharField(max_length=250,choices=cxr_CHOICES,null=True, blank=True)
    other_cxr_year=models.IntegerField(null=True, blank=True)
    other_cxr_month=models.IntegerField(null=True, blank=True)
    other_cxr_day=models.IntegerField(null=True, blank=True)

    ecg_CHOICES = [('normal', 'نرمال'),('not_normal','غیر نرمال'),('not_ekhtesasi','تغییرات غیر اختصاصی'),('again','نیاز به تکرار')]
    other_ecg = models.CharField(max_length=250,choices=ecg_CHOICES, null=True, blank=True)
    other_ecg_year=models.IntegerField(null=True, blank=True)
    other_ecg_month=models.IntegerField(null=True, blank=True)
    other_ecg_day=models.IntegerField(null=True, blank=True)
    other_result = models.CharField(max_length=250, null=True, blank=True)


class Consulting_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='consulting',null=True,blank=True) 
    first_year=models.IntegerField(null=True, blank=True)
    first_month=models.IntegerField(null=True, blank=True)
    first_day=models.IntegerField(null=True, blank=True)
    first_reason = models.CharField(max_length=250, null=True, blank=True)
    first_type = models.CharField(max_length=250, null=True, blank=True)
    first_result = models.CharField(max_length=250, null=True, blank=True)
    second_year=models.IntegerField(null=True, blank=True)
    second_month=models.IntegerField(null=True, blank=True)
    second_day=models.IntegerField(null=True, blank=True)
    second_reason = models.CharField(max_length=250, null=True, blank=True)
    second_type = models.CharField(max_length=250, null=True, blank=True)
    second_result = models.CharField(max_length=250, null=True, blank=True)


class Final_Theory_Model(models.Model):
    person = models.ForeignKey(Personal_Species_Model, on_delete=models.CASCADE,related_name='final',null=True,blank=True) 
    belamane = models.BooleanField(default=False)
    mashrot = models.BooleanField(default=False)
    mashrot_reason = models.CharField(max_length=250, null=True, blank=True)
    rad = models.BooleanField(default=False)
    rad_reason = models.CharField(max_length=250, null=True, blank=True)
    recommendations = models.CharField(max_length=250, null=True, blank=True)
    reason = models.CharField(max_length=250, null=True, blank=True)
    problems = models.CharField(max_length=250, null=True, blank=True)
    d_code = models.IntegerField(null=True, blank=True)
