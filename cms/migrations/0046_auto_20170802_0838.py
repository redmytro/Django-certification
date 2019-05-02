# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 12:38
from __future__ import unicode_literals

from django.db import migrations


def reslug(apps, schema_editor):
    CorpPage = apps.get_model('cms', 'CorpPage')

    parent = CorpPage.objects.get(full_path='membership')
    page = CorpPage.objects.get(full_path='about/our-clubs')
    page.parent = parent
    page.full_path = 'membership/our-clubs'
    page.is_locked = True
    page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0045_auto_20170802_0304'),
    ]

    operations = [
        migrations.RunPython(reslug),
    ]