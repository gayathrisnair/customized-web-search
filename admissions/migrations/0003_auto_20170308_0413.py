# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-08 04:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_admission_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='details',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='offered_by',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='url',
        ),
    ]
