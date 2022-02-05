# Generated by Django 4.0 on 2022-02-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0004_alter_summary_of_results_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary_of_results',
            name='ALT',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='ALT_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='AST',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='AST_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='PSA',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='PSA_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='TSH',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='TSH_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='age_two',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_lead',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('تغییرات غیر اختصاصی', 'تغییرات غیر اختصاصی'), ('نیاز به تکرار', 'نیاز به تکرار'), ('غیر نرمال', 'غیر نرمال'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_lead_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_pressure',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_pressure_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_sugar',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='blood_sugar_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='body_mass',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='body_mass_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='breast_photo',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('غیر نرمال', 'غیر نرمال'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='breathing_test',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('تحدیدی', 'تحدیدی'), ('انسدادی', 'انسدادی'), ('نیاز به تکرار', 'نیاز به تکرار'), ('namaie_toaman', 'نمای توامان تحدیدی وانسدادی'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='cholesterol',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='cholesterol_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='code',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='color_vision',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('غیر نرمال', 'غیر نرمال'), ('تشخیص رنگ قرمز', 'تشخیص رنگ قرمز'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='depth_vision',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('غیر نرمال', 'غیر نرمال'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='duration_of_employment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='field_of_veiw',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('غیر نرمال', 'غیر نرمال'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='final_theory',
            field=models.CharField(choices=[('null', ''), ('بلامانع', 'بلامانع'), ('تغییر شغل', 'تغییر شغل'), ('مشروط', 'مشروط'), ('کمیسیون', 'کمیسیون')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='harmful_factors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='job',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='left_ear_hearing',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('کاهش شنوایی هدایتی', 'کاهش شنوایی هدایتی'), ('کاهش شنوایی حسی عصبی', 'کاهش شنوایی حسی عصبی'), ('کاهش شنوایی ناشی از صدا', 'کاهش شنوایی ناشی از صدا'), ('توامان هدایتی و حسی عصبی', 'توامان هدایتی و حسی عصبی'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='left_eye_vision',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='left_eye_vision_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='left_eye_vision_with_glasses',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='length',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='occupational_actions',
            field=models.CharField(choices=[('null', ''), ('درحال پیگیری', 'درحال پیگیری'), ('انجام شده', 'انجام شده'), ('انجام نشده', 'انجام نشده')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='occupational_disease_code',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='overweight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='problem',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='problems_with_the_persons_job',
            field=models.CharField(choices=[('null', ''), ('دارد', 'دارد'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='recommendations',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='refer_to_specialist',
            field=models.CharField(choices=[('null', ''), ('ندارد', 'ندارد'), ('قلب و عروق', 'قلب و عروق'), ('داخلی', 'داخلی'), ('ریه', 'ریه'), ('غدد', 'غدد'), ('سایر', 'سایر')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='reson_for_opening_the_case',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='right_ear_hearing',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('کاهش شنوایی هدایتی', 'کاهش شنوایی هدایتی'), ('کاهش شنوایی حسی عصبی', 'کاهش شنوایی حسی عصبی'), ('کاهش شنوایی ناشی از صدا', 'کاهش شنوایی ناشی از صدا'), ('توامان هدایتی و حسی عصبی', 'توامان هدایتی و حسی عصبی'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='right_eye_vision',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='right_eye_vision_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='right_eye_vision_with_glasses',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='start_month',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='start_year',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='triglyceride',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='triglyceride_status',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='urine',
            field=models.CharField(choices=[('null', ''), ('نرمال', 'نرمال'), ('غیر نرمال', 'غیر نرمال'), ('ندارد', 'ندارد')], default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='summary_of_results',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
