# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_words', models.CharField(blank=True, max_length=255, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255, unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('main_image', models.FileField(upload_to='galleries/%Y/%m')),
            ],
            options={
                'verbose_name': 'Фотогалерея',
                'verbose_name_plural': 'Фотогалереи',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(upload_to='photos/%Y/%m')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Gallery')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
