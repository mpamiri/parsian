# Generated by Django 4.0 on 2022-04-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0015_personal_species_model_raste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='audio_l_sds',
        ),
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='audio_l_srt',
        ),
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='audio_r_sds',
        ),
        migrations.RemoveField(
            model_name='para_clinic_model',
            name='audio_r_srt',
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_eight_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_eight_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_five_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_five_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_four_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_four_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_one_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_one_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_six_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_six_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_two_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_l_two_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_eight_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_eight_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_five_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_five_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_four_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_four_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_one_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_one_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_six_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_six_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_two_ac',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='para_clinic_model',
            name='audio_r_two_bc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]