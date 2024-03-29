# Generated by Django 4.0 on 2022-07-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0018_remove_experiments_model_bun_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiments_model',
            name='ppd',
        ),
        migrations.RemoveField(
            model_name='experiments_model',
            name='se',
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='alk_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='alt_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ast_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cbc_hb_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cbc_htc_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cbc_plt_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cbc_rbc_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cbc_wbc_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='chol_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='cr_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='d_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='fbs_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='hdl_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ldl_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='lead_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ppd_status',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('not_normal', 'غیر نرمال')], default='normal', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='psa_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='se_status',
            field=models.CharField(blank=True, choices=[('normal', 'نرمال'), ('not_normal', 'غیر نرمال')], default='normal', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='tg_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='tsh_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ua_bact_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ua_glu_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ua_rbc_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='experiments_model',
            name='ua_wbc_status',
            field=models.BooleanField(default=False),
        ),
    ]
