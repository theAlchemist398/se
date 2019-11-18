# Generated by Django 2.1.5 on 2019-11-18 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20191118_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='name',
            new_name='flight_name',
        ),
        migrations.AddField(
            model_name='session',
            name='username',
            field=models.CharField(default='user123', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(13, 11, 41, 150272)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 18, 13, 11, 41, 150219)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.time(13, 11, 41, 150245)),
        ),
    ]
