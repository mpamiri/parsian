# Generated by Django 4.0 on 2022-07-02 11:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0014_job_history_model_durations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment_model',
            name='date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assessment_model',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assessment_model',
            name='date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='blood_pressure',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='length',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='pulse',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='weight',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='examinationscourse',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='alk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='alt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ast',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='bun',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_hb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_htc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_plt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_rbc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_wbc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='chol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='fbs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='first_date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='first_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='first_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='hbs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='hdl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ldl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ppd',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='se',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='second_date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='second_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='second_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='tg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='third_date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='third_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='third_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_bact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_glu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_prot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_rbc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_wbc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_eight_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_eight_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_five_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_five_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_four_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_four_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_one_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_one_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_six_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_six_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_two_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_two_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_eight_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_eight_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_five_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_five_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_four_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_four_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_one_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_one_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_six_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_six_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_two_ac',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_two_bc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_hedat_l_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_hedat_l_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_hedat_r_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_hedat_r_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_meidan_hedat_l_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_meidan_hedat_l_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_meidan_hedat_r_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_meidan_hedat_r_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_omgh',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_rangi_hedat_l_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_rangi_hedat_l_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_rangi_hedat_r_ba',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='opto_rangi_hedat_r_bi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_cxr_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_cxr_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_cxr_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_ecg_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_ecg_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_ecg_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1300), django.core.validators.MaxValueValidator(1400)]),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='children',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='date_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='date_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='date_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='employment_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='examinations_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsianapp.examinationscourse'),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='personal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='profil_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='ALT',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='AST',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='D3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='PSA',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='TSH',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='age_two',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='blood_lead',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='chratinin',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='summary_of_results_model',
            name='number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
