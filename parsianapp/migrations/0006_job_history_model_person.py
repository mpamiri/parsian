# Generated by Django 4.0 on 2022-06-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0005_consulting_model_person_examinations_model_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_history_model',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='parsianapp.personal_species_model'),
        ),
    ]
