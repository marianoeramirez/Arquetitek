# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 16:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170818_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='autor',
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 18, 16, 56, 45, 59312, tzinfo=utc)),
        ),
    ]