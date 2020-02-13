# Generated by Django 2.2.4 on 2019-09-14 05:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190914_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 5, 17, 48, 873318, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]