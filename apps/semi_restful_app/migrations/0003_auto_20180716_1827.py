# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-16 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0002_auto_20180713_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
