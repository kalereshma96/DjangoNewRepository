# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-26 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]