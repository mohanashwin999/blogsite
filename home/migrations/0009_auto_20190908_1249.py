# Generated by Django 2.2.4 on 2019-09-08 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190908_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 49, 47, 794829)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 12, 49, 47, 795826)),
        ),
    ]
