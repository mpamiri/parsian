# Generated by Django 4.0 on 2022-04-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0016_remove_para_clinic_model_audio_l_sds_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_species_model',
            name='fathers_name',
            field=models.CharField(blank=True, default='ذکر نشده', max_length=20, null=True),
        ),
    ]