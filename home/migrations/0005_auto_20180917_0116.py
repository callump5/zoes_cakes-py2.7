# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import home.upload_to_aws


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180910_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='awefoluwhqef ohwqefh 9ouqwehf0 iwqehf 0qhwei0fh poiweeqjnfpi jq3pierhfg 0iqhwe0fh 0iwehf 0iqwhei0f 093wq ehfg 0ihweqripfg poihweofwqef'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null='True', upload_to=home.upload_to_aws.upload_img),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null='True', upload_to=home.upload_to_aws.upload_img),
        ),
    ]
