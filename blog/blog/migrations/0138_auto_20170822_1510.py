# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 19:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0137_auto_20170822_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 22, 19, 10, 29, 902915, tzinfo=utc)),
        ),
    ]