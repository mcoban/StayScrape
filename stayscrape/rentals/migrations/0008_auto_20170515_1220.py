# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_auto_20170515_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='title',
            new_name='title_preffix',
        ),
    ]
