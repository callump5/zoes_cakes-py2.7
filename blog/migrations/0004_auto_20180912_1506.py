# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180910_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 15, 6, 29, 481000)),
        ),
    ]
