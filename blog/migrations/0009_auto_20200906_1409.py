# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-06 08:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200906_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 6, 8, 39, 49, 35006, tzinfo=utc)),
        ),
    ]
