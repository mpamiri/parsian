# Generated by Django 4.0 on 2022-08-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0047_disease_model_p_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease_model',
            name='e_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='e_examinations_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='e_fathers_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='e_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='disease_model',
            name='e_personal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
