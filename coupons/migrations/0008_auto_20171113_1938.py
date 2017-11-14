# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0007_auto_20151105_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='bulk',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupon',
            name='bulk_length',
            field=models.PositiveIntegerField(default=8),
        ),
        migrations.AddField(
            model_name='coupon',
            name='bulk_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='bulk_seed',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='couponuser',
            name='code',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Bulk Code'),
        ),
    ]
