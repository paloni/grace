# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20171130_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Настройка сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
