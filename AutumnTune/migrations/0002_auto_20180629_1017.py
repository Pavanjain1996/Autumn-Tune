# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-29 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutumnTune', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.CharField(default='Party', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='language',
            field=models.CharField(default='Hindi', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='typeof',
            field=models.CharField(default='Singing', max_length=100),
        ),
    ]
