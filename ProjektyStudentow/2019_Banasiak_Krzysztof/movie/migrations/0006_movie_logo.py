# Generated by Django 2.2.1 on 2019-05-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20190509_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='logo',
            field=models.CharField(default=1.0, max_length=1000),
            preserve_default=False,
        ),
    ]