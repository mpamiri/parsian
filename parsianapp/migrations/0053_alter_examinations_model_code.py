# Generated by Django 4.1.3 on 2022-11-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0052_auto_20221017_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinations_model',
            name='code',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
