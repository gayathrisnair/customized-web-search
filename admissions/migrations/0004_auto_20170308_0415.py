# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-08 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_auto_20170308_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='catagory',
            field=models.CharField(default='male', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='details',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='offered_by',
            field=models.CharField(default='-', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='qualifications',
            field=models.CharField(default='-', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admission',
            name='url',
            field=models.URLField(default='-'),
            preserve_default=False,
        ),
    ]
