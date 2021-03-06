# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered_by', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=150)),
                ('qualification', models.CharField(max_length=150)),
                ('catagory', models.CharField(max_length=150)),
                ('annual_income', models.CharField(max_length=150)),
                ('last_date', models.CharField(max_length=150)),
                ('details', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]
