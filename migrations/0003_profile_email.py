# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donatelove', '0002_auto_20180918_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]
