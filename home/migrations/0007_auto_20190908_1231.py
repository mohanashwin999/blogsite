# Generated by Django 2.2.4 on 2019-09-08 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190908_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='lname',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 31, 11, 890790)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 31, 11, 891791)),
        ),
    ]
