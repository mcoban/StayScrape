# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.IntegerField(default=0)),
                ('rental_id', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('sleeps', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionId', models.IntegerField(default=0)),
                ('location', models.CharField(default='', max_length=250)),
                ('regionArray', models.CharField(default='', max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('sleeps', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('detailPageUrl', models.CharField(max_length=250, unique=True)),
                ('galleryUrl', models.CharField(default='', max_length=250)),
                ('geoCode', models.CharField(default='', max_length=50)),
                ('shortJSON', models.TextField(default='')),
                ('longJSON', models.TextField(default='')),
                ('is_checked', models.BooleanField(default=False)),
                ('averageRating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('reviewCount', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('slug', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='relations',
            unique_together=set([('rental_id', 'place_id')]),
        ),
    ]
