# Generated by Django 2.1.5 on 2019-04-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitconv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convfactor',
            name='lbs_to_t_oz',
            field=models.DecimalField(decimal_places=2, default=14.58, max_digits=4),
        ),
        migrations.AlterField(
            model_name='convfactor',
            name='t_oz_to_lbs',
            field=models.DecimalField(decimal_places=6, default=0.06857, max_digits=6),
        ),
    ]