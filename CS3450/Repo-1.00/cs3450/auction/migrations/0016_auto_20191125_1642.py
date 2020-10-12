# Generated by Django 2.2.5 on 2019-11-25 23:42

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0015_auto_20191125_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_silent_item',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='silentauction',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 3, 42, 40, 75307, tzinfo=utc), verbose_name='End Time'),
        ),
    ]
