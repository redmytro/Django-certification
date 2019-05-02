# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-26 06:23
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0022_auto_20170326_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='listing_image',
            field=models.ImageField(blank=True, null=True, upload_to=clublink.base.utils.RandomizedUploadPath('listing_image')),
        ),
        migrations.AlterField(
            model_name='club',
            name='dark_logo',
            field=models.ImageField(blank=True, null=True, upload_to=clublink.base.utils.RandomizedUploadPath('dark_logos')),
        ),
    ]
