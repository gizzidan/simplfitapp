# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
