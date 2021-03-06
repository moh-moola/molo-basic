# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-20 11:49
from __future__ import unicode_literals

from django.conf import settings as django_settings
from django.db import migrations, models
import django.db.models.deletion

from molo.core.models import CmsSettings, Timezone

from wagtail.core.models import Site


def set_initial_timezone(apps, schema_editor):
    current_timezone_name = django_settings.TIME_ZONE or 'UTC'
    for site in Site.objects.all():
        cms_settings = CmsSettings.for_site(site)
        cms_settings.timezone = Timezone.objects.filter(
            title=current_timezone_name,
        ).first()
        cms_settings.save()


def unset_timezone(apps, schema_editor):
    for site in Site.objects.all():
        site_settings = CmsSettings.for_site(site)
        site_settings.timezone = None
        site_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0005_data_migration_promoted_articles'),
    ]

    operations = [
        migrations.RunPython(set_initial_timezone, unset_timezone),
    ]
