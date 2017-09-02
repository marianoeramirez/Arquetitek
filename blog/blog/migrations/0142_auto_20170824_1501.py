# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 19:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0141_auto_20170824_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog/fotos/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateField(default=datetime.datetime(2017, 8, 24, 19, 1, 16, 803723, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]