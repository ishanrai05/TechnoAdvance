# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-03 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techx', '0012_auto_20180704_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_a_workshop',
            old_name='conact_number',
            new_name='contact_number',
        ),
    ]