# Generated by Django 4.0 on 2022-02-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0011_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary_of_results',
            name='job_code',
            field=models.CharField(blank=True, default=0, max_length=30, null=True),
        ),
    ]
