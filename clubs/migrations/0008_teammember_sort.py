# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 13:27
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_auto_20170216_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='sort',
            field=models.IntegerField(default=0),
        ),
    ]
