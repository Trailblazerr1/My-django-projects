# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-02 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
