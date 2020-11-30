# Generated by Django 2.0.7 on 2020-11-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0008_auto_20201109_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='u10coupon',
            field=models.IntegerField(default=0, verbose_name='十元优惠券'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='u20coupon',
            field=models.IntegerField(default=0, verbose_name='二十元优惠券'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='u30coupon',
            field=models.IntegerField(default=0, verbose_name='三十元优惠券'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uconsumed',
            field=models.IntegerField(default=0, verbose_name='已消费金额'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
    ]
