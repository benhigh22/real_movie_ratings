# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 21:05
from __future__ import unicode_literals

from django.db import migrations

from movieratings_app.models import Rater


def load_data(*args):
   with open("data/ml-100k/u.user") as users:
       for user in users.readlines():
           line= user.split("|")
           Rater.objects.create(id=line[0], age=line[1],
                                gender=line[2], occupation=line[3],
                                zip_code=line[4])


class Migration(migrations.Migration):

   dependencies = [
       ('movieratings_app', '0001_initial'),
   ]


   operations = [
       migrations.RunPython(load_data)
   ]