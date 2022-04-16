# Generated by Django 4.0 on 2022-04-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0017_alter_personal_species_model_fathers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment_model',
            name='kar_shenas',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assessment_model',
            name='kar_shenas_name',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assessment_model',
            name='required_description',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='first_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='consulting_model',
            name='second_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='asabi_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='colie_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='eskelety_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='eye_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='ghalb_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='gosh_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='local_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='other',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='ravan_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='rie_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='sar_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='shekam_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='examinations_model',
            name='skin_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='first_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='first_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='second_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='second_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='third_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='third_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='final_theory_model',
            name='mashrot_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='final_theory_model',
            name='rad_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='final_theory_model',
            name='recommendations',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='current_job',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='current_job_duty',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='current_job_from',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='current_job_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='current_job_to',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='previous_job',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='previous_job_duty',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='previous_job_from',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='previous_job_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='previous_job_to',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_current_job',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_current_job_duty',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_current_job_from',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_current_job_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_current_job_to',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_previous_job',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_previous_job_duty',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_previous_job_from',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_previous_job_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job_history_model',
            name='second_previous_job_to',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_fef',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_fev',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_fevvfvc',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_fvc',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_pef',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_tafsir',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_vext',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_cxr',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_ecg',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_result',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='oudio_tafsir',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='eighth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='eleventh_des_duration',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='eleventh_des_number',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='fifteenth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='fifth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='first_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='fourteenth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='fourth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='ninth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='second_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='seventh_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='sixteenth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='sixth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='tenth_des_duration',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='tenth_des_number',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='third_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='thirteenth_des_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='thirteenth_des_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_history_model',
            name='twelfth_des',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='address',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='employer_name',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='examinations_type',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='job_name',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='medical_exemption_reason',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='name',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='personal_species_model',
            name='raste',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True),
        ),
    ]