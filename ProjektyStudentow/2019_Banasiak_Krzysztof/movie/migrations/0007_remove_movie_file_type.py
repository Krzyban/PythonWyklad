# Generated by Django 2.2.1 on 2019-05-09 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='file_type',
        ),
    ]
