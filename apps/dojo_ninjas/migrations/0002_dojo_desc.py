# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-17 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
