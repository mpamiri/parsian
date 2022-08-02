# Generated by Django 4.0 on 2022-07-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0020_alter_experiments_model_alk_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinations_model',
            name='body_mass',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='disease_model',
            name='order_number',
            field=models.IntegerField(choices=[(1, '1'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='examinationscourse',
            name='doctor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='examinationscourse',
            name='employer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]