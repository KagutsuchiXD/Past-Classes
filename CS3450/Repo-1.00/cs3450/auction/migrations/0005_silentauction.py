# Generated by Django 2.2.6 on 2019-11-13 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_bidhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SilentAuction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_active', models.BooleanField(default=False)),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
            ],
        ),
    ]