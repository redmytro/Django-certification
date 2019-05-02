# Generated by Django 2.0.2 on 2018-02-26 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('cms', '0085_auto_20180309_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpeventsgallery',
            name='site',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_galleries', to='sites.Site'),
        ),
    ]
