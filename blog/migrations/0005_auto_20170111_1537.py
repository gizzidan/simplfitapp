# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
