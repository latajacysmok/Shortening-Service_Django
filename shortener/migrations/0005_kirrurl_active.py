# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-22 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20180222_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]