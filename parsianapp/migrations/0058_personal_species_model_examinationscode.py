# Generated by Django 4.2 on 2023-05-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0057_examinationscourse_companyname_alter_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_species_model',
            name='ExaminationsCode',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
