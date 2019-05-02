# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-14 09:33
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.storages
import clublink.cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0067_auto_20170814_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=clublink.base.storages.S3Boto3StorageAssets(base_url='/asset_files/', location='/var/www/clublink/asset_files'), upload_to=clublink.cms.models.get_file_upload_path),
        ),
    ]