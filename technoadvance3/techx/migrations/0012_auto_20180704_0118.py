# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-03 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techx', '0011_auto_20180702_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_a_workshop',
            name='designation',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='location',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='request_a_workshop',
            name='workshop',
            field=models.TextField(max_length=100, null=True),
        ),
    ]