# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-01 21:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techx', '0009_auto_20180702_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_a_workshop',
            name='conact_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='institute_name',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='workshop',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='your_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='your_name',
            field=models.CharField(max_length=100),
        ),
    ]
