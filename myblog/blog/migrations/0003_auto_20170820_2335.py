# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='logtime',
            field=models.CharField(max_length=30),
        ),
    ]
