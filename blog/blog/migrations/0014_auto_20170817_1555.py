# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 19:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170817_1123'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 19, 55, 18, 375652, tzinfo=utc)),
        ),
    ]