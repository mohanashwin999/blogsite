# Generated by Django 2.2.4 on 2019-10-05 11:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20191005_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 5, 11, 11, 8, 574518, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 5, 11, 11, 8, 573518, tzinfo=utc)),
        ),
    ]