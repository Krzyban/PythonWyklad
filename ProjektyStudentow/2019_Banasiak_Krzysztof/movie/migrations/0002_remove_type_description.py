# Generated by Django 2.2.1 on 2019-05-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='description',
        ),
    ]
