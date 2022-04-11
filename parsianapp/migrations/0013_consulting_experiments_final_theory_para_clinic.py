# Generated by Django 4.0 on 2022-04-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0012_examinations_model_asabi_des_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_year', models.IntegerField(blank=True, default=0, null=True)),
                ('first_month', models.IntegerField(blank=True, default=0, null=True)),
                ('first_day', models.IntegerField(blank=True, default=0, null=True)),
                ('first_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('first_type', models.CharField(blank=True, max_length=50, null=True)),
                ('first_result', models.CharField(blank=True, max_length=50, null=True)),
                ('second_year', models.IntegerField(blank=True, default=0, null=True)),
                ('second_month', models.IntegerField(blank=True, default=0, null=True)),
                ('second_day', models.IntegerField(blank=True, default=0, null=True)),
                ('second_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('second_type', models.CharField(blank=True, max_length=50, null=True)),
                ('second_result', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('cbc_wbc', models.IntegerField(blank=True, default=0, null=True)),
                ('cbc_rbc', models.IntegerField(blank=True, default=0, null=True)),
                ('cbc_hb', models.IntegerField(blank=True, default=0, null=True)),
                ('cbc_htc', models.IntegerField(blank=True, default=0, null=True)),
                ('cbc_plt', models.IntegerField(blank=True, default=0, null=True)),
                ('ua_prot', models.IntegerField(blank=True, default=0, null=True)),
                ('ua_glu', models.IntegerField(blank=True, default=0, null=True)),
                ('ua_rbc', models.IntegerField(blank=True, default=0, null=True)),
                ('ua_wbc', models.IntegerField(blank=True, default=0, null=True)),
                ('ua_bact', models.IntegerField(blank=True, default=0, null=True)),
                ('fbs', models.IntegerField(blank=True, default=0, null=True)),
                ('chol', models.IntegerField(blank=True, default=0, null=True)),
                ('ldl', models.IntegerField(blank=True, default=0, null=True)),
                ('hdl', models.IntegerField(blank=True, default=0, null=True)),
                ('tg', models.IntegerField(blank=True, default=0, null=True)),
                ('bun', models.IntegerField(blank=True, default=0, null=True)),
                ('cr', models.IntegerField(blank=True, default=0, null=True)),
                ('alt', models.IntegerField(blank=True, default=0, null=True)),
                ('ast', models.IntegerField(blank=True, default=0, null=True)),
                ('alk', models.IntegerField(blank=True, default=0, null=True)),
                ('hbs', models.IntegerField(blank=True, default=0, null=True)),
                ('se', models.IntegerField(blank=True, default=0, null=True)),
                ('ppd', models.IntegerField(blank=True, default=0, null=True)),
                ('first_type', models.CharField(blank=True, max_length=50, null=True)),
                ('first_result', models.CharField(blank=True, max_length=50, null=True)),
                ('first_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('first_date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('first_date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('second_type', models.CharField(blank=True, max_length=50, null=True)),
                ('second_result', models.CharField(blank=True, max_length=50, null=True)),
                ('second_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('second_date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('second_date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('third_type', models.CharField(blank=True, max_length=50, null=True)),
                ('third_result', models.CharField(blank=True, max_length=50, null=True)),
                ('third_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('third_date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('third_date_day', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Final_Theory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belamane', models.BooleanField(default=False)),
                ('mashrot', models.BooleanField(default=False)),
                ('mashrot_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('rad', models.BooleanField(default=False)),
                ('rad_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Para_Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opto_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_hedat_r_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_hedat_r_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_hedat_l_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_hedat_l_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_rangi_hedat_r_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_rangi_hedat_r_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_rangi_hedat_l_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_rangi_hedat_l_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_meidan_hedat_r_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_meidan_hedat_r_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_meidan_hedat_l_ba', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_meidan_hedat_l_bi', models.IntegerField(blank=True, default=0, null=True)),
                ('opto_omgh', models.IntegerField(blank=True, default=0, null=True)),
                ('audio_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('audio_date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('audio_date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('oudio_tafsir', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_sds', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_srt', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_eight_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_eight_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_six_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_six_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_four_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_four_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_two_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_two_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_one_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_one_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_five_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_r_five_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_sds', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_srt', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_eight_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_eight_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_six_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_six_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_four_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_four_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_two_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_two_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_one_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_one_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_five_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('audio_l_five_bc', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_date_year', models.IntegerField(blank=True, default=0, null=True)),
                ('espiro_date_month', models.IntegerField(blank=True, default=0, null=True)),
                ('espiro_date_day', models.IntegerField(blank=True, default=0, null=True)),
                ('espiro_fevvfvc', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_fev', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_fvc', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_vext', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_pef', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_fef', models.CharField(blank=True, max_length=50, null=True)),
                ('espiro_tafsir', models.CharField(blank=True, max_length=50, null=True)),
                ('other_cxr', models.CharField(blank=True, max_length=50, null=True)),
                ('other_cxr_year', models.IntegerField(blank=True, default=0, null=True)),
                ('other_cxr_month', models.IntegerField(blank=True, default=0, null=True)),
                ('other_cxr_day', models.IntegerField(blank=True, default=0, null=True)),
                ('other_ecg', models.CharField(blank=True, max_length=50, null=True)),
                ('other_ecg_year', models.IntegerField(blank=True, default=0, null=True)),
                ('other_ecg_month', models.IntegerField(blank=True, default=0, null=True)),
                ('other_ecg_day', models.IntegerField(blank=True, default=0, null=True)),
                ('other_result', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]