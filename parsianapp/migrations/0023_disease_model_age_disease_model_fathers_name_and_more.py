# Generated by Django 4.0 on 2022-07-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0022_experiments_model_ua_prot_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease_model',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='personal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_cxr',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('not_normal', 'غیر نرمال')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='other_ecg',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('not_normal', 'غیر نرمال'), ('not_ekhtesasi', 'تغییرات غیر اختصاصی'), ('again', 'نیاز به تکرار')], max_length=50, null=True),
        ),
    ]