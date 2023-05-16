# Generated by Django 4.2 on 2023-05-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0058_personal_species_model_examinationscode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examinations_model',
            old_name='blood_pressure',
            new_name='blood_pressure_bot',
        ),
        migrations.AddField(
            model_name='examinations_model',
            name='blood_pressure_top',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
