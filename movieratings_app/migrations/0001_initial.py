# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=30)),
                ('release_date', models.CharField(max_length=30)),
                ('video_release_date', models.CharField(blank=True, default='', max_length=30)),
                ('imdb', models.URLField()),
                ('unknown_genre', models.BooleanField(default=0)),
                ('action', models.BooleanField(default=0)),
                ('adventure', models.BooleanField(default=0)),
                ('animation', models.BooleanField(default=0)),
                ('childrens', models.BooleanField(default=0)),
                ('comedy', models.BooleanField(default=0)),
                ('crime', models.BooleanField(default=0)),
                ('documentary', models.BooleanField(default=0)),
                ('drama', models.BooleanField(default=0)),
                ('fantasy', models.BooleanField(default=0)),
                ('filmnoir', models.BooleanField(default=0)),
                ('horror', models.BooleanField(default=0)),
                ('musical', models.BooleanField(default=0)),
                ('mystery', models.BooleanField(default=0)),
                ('romance', models.BooleanField(default=0)),
                ('scifi', models.BooleanField(default=0)),
                ('thriller', models.BooleanField(default=0)),
                ('war', models.BooleanField(default=0)),
                ('western', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=2)),
                ('occupation', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings_app.Movie')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings_app.Rater')),
            ],
        ),
    ]
