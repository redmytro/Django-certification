# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-08 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0078_club_membership_brochure'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='use_corp_styles',
            field=models.BooleanField(default=False, help_text='This is meant to use the same background as your corp-page equivalent based on the path'),
        ),
    ]
