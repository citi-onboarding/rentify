# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Model', models.CharField(max_length=30)),
                ('Year', models.CharField(max_length=4)),
                ('Plate', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Availability', models.BooleanField()),
            ],
        ),
    ]