# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170106_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
