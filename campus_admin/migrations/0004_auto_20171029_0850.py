# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-29 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0003_auto_20171029_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterNos',
            field=models.CharField(default='', max_length=20),
        ),
    ]