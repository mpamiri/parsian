# Generated by Django 4.0 on 2022-07-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0026_rename_oudio_tafsir_para_clinic_model_oudio_l_tafsir_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='oudio_l_tafsir',
        ),
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='oudio_r_tafsir',
        ),
        migrations.AddField(
            model_name='para_clinic_model',
            name='audio_l_tafsir',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'), ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'), ('kahesh_shenavai_nashi_az_seda', 'کاهش شنوایی ناشی از صدا'), ('toaman_hedayati_va_hesi_asabi', 'توامان هدایتی و حسی عصبی')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='para_clinic_model',
            name='audio_r_tafsir',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('kahesh_shenavai_hedayati', 'کاهش شنوایی هدایتی'), ('kahesh_shenavai_hesi_asabi', 'کاهش شنوایی حسی عصبی'), ('kahesh_shenavai_nashi_az_seda', 'کاهش شنوایی ناشی از صدا'), ('toaman_hedayati_va_hesi_asabi', 'توامان هدایتی و حسی عصبی')], max_length=50, null=True),
        ),
    ]