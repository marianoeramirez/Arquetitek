# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 20:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0098_auto_20170821_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 21, 20, 42, 21, 595256, tzinfo=utc)),
        ),
    ]