# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0007_auto_20171029_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='acadYear',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.IntegerField(default=''),
        ),
    ]
