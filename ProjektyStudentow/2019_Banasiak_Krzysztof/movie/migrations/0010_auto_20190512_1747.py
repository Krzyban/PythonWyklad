# Generated by Django 2.2.1 on 2019-05-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20190509_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='type',
        ),
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.ForeignKey(default=1.0, on_delete=django.db.models.deletion.CASCADE, to='movie.Type'),
            preserve_default=False,
        ),
    ]
