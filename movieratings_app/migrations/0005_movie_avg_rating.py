# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings_app', '0004_auto_20160225_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(null=True),
        ),
    ]
