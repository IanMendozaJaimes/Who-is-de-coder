# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_equipos_tecnologias'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='github',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipos',
            name='url',
            field=models.URLField(default='', max_length=255),
        ),
    ]