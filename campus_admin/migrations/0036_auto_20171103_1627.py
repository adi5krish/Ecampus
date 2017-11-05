# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus_admin', '0035_auto_20171102_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registers',
            name='studentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registers_studentId', to='campus_admin.Student'),
        ),
    ]
