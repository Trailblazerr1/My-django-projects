# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_play_he'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='pop',
            field=models.IntegerField(default=100),
        ),
    ]
