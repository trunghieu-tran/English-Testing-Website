# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testEng', '0007_auto_20160515_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='audio',
            field=models.FileField(default='', upload_to=''),
        ),
    ]