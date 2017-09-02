# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 21:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0144_auto_20170824_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AddField(
            model_name='foto',
            name='video',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 24, 21, 38, 4, 392564, tzinfo=utc)),
        ),
    ]