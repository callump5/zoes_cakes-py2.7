# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-06 20:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_item_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorys',
            old_name='url',
            new_name='slug',
        ),
    ]