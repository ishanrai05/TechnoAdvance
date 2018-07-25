# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-01 20:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('techx', '0006_auto_20180701_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_a_workshop',
            name='message',
            field=models.CharField(default=datetime.datetime(2018, 7, 1, 20, 26, 20, 977976, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request_a_workshop',
            name='subject',
            field=models.CharField(default='null', max_length=1000),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='conact_number',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='designation',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='institute_name',
            field=models.TextField(default='null', max_length=500),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='location',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='workshop',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='your_email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='your_name',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]