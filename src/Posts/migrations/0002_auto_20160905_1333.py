# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-05 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(upload_to='./'),
        ),
    ]