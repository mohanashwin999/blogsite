# Generated by Django 2.2.4 on 2019-09-08 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190908_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 47, 34, 151872)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 47, 34, 152872)),
        ),
    ]
