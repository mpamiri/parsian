# Generated by Django 4.0 on 2022-07-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0017_alter_para_clinic_model_espiro_tafsir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiments_model',
            name='bun',
        ),
        migrations.RemoveField(
            model_name='experiments_model',
            name='hbs',
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='d',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='lead',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='psa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='tsh',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='espiro_tafsir',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('ensedadi', 'انسدادی'), ('tahdidi', 'تحدیدی'), ('ensedadivtahdidi', 'انسدادی و تحدیدی'), ('again', 'نیاز به تکرار')], max_length=50, null=True),
        ),
    ]
