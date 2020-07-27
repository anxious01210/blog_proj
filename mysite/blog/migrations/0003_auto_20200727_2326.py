# Generated by Django 3.0.3 on 2020-07-27 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200727_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 20, 26, 32, 503600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
