# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0040_auto_20171103_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='acadYear',
            field=models.CharField(default='', max_length=200),
        ),
    ]
