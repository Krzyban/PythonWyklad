# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0005_auto_20180509_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapisy',
            name='day_choice',
            field=models.CharField(choices=[('1', 'Modern jazz'), ('2', 'Modern balet'), ('3', 'Afro dance'), ('4', 'Break dance')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='zapisy',
            name='hour_choice',
            field=models.CharField(choices=[('1', 'Modern jazz'), ('2', 'Modern balet'), ('3', 'Afro dance'), ('4', 'Break dance')], max_length=1, null=True),
        ),
    ]