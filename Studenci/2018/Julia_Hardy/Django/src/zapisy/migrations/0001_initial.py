# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zajecia', '0004_auto_20180507_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapisy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zajecia.Zajecia')),
            ],
        ),
    ]