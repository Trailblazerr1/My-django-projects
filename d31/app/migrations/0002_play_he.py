# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='he',
            field=models.IntegerField(default=170),
        ),
    ]
