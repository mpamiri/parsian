# Generated by Django 4.0 on 2022-04-08 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0006_alter_summary_of_results_right_ear_hearing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examinations_type', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('profil_number', models.IntegerField(blank=True, default=0, null=True)),
                ('employment_number', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('fathers_name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('mard', 'مرد'), ('zan', 'زن')], default='mard', max_length=20, null=True)),
                ('marriage_status', models.CharField(blank=True, choices=[('mojarad', 'مجرد'), ('motahel', 'متاحل')], default='mojarad', max_length=20, null=True)),
                ('children', models.IntegerField(blank=True, default=0, null=True)),
                ('age', models.IntegerField(blank=True, default=1300, null=True, validators=[django.core.validators.MinValueValidator(1300), django.core.validators.MaxValueValidator(1400)])),
                ('personal_code', models.IntegerField(blank=True, default=0, null=True)),
                ('military_status', models.CharField(blank=True, choices=[('khedmat_karde', 'خدمت کرده'), ('moaf', 'معاف')], default='khedmat_karde', max_length=20, null=True)),
                ('medical_exemption', models.BooleanField(default=False)),
                ('medical_exemption_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('job_name', models.CharField(blank=True, max_length=20, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='submit_company',
            old_name='specialist',
            new_name='employer',
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='gender',
            field=models.CharField(choices=[('mard', 'مرد'), ('zan', 'زن')], default='mard', max_length=20, null=True),
        ),
    ]