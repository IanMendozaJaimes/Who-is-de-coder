# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaton', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackaton',
            name='organizadores',
            field=models.ManyToManyField(to='users.Organizador'),
        ),
    ]