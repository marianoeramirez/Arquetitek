# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 17:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170818_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 18, 17, 35, 25, 698052, tzinfo=utc)),
        ),
    ]