# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-26 11:31
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0013_certificatetype_restrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetype',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]