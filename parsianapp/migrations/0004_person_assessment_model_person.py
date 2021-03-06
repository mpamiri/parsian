# Generated by Django 4.0 on 2022-06-27 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0003_disease_model_examinations_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('melli_code', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='assessment_model',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessment', to='parsianapp.personal_species_model'),
        ),
    ]
