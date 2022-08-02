# Generated by Django 4.0 on 2022-07-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsianapp', '0019_remove_experiments_model_ppd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiments_model',
            name='alk_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='alt_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ast_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_hb_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_htc_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_plt_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_rbc_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cbc_wbc_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='chol_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='cr_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='d_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='fbs_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='hdl_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ldl_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='lead_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='psa_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='tg_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='tsh_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_bact_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_glu_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_rbc_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='experiments_model',
            name='ua_wbc_status',
            field=models.BooleanField(default=True),
        ),
    ]