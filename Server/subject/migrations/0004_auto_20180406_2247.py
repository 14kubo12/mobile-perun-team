# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-06 20:47
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20180406_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='when',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tape',
            name='stt_output',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tape',
            name='text',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]
