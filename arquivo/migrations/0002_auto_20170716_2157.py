# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
