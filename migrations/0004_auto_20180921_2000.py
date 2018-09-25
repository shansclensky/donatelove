# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 20:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donatelove', '0003_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_organsation',
            new_name='is_organisation',
        ),
        migrations.AddField(
            model_name='organisationcorpusfund',
            name='organisation',
            field=models.OneToOneField(default=b'', on_delete=django.db.models.deletion.CASCADE, to='donatelove.Organisation'),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(default=b'', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdonation',
            name='user',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donations_required',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='organisationexpenditurelog',
            name='organisation',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='donatelove.Organisation'),
        ),
        migrations.AlterField(
            model_name='userdonation',
            name='organisation',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='donatelove.Organisation'),
        ),
    ]
