# Generated by Django 2.1.5 on 2019-11-18 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20191118_1318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(14, 4, 41, 196119)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 14, 4, 41, 196069)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.time(14, 4, 41, 196091)),
        ),
    ]