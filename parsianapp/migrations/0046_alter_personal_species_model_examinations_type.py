# Generated by Django 4.0 on 2022-08-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0045_remove_job_history_model_current_job_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_species_model',
            name='examinations_type',
            field=models.CharField(blank=True, choices=[('badv_estekhdam', 'بدو استخدام'), ('dore_e', 'دوره ای'), ('bazgasht_be_kar', 'بازگشت به کار')], max_length=250, null=True),
        ),
    ]
