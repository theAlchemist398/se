# Generated by Django 2.1.5 on 2019-11-17 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airlines', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('departure_date', models.DateField(default=datetime.datetime(2019, 11, 17, 14, 5, 7, 270285))),
                ('departure_time', models.TimeField(default=datetime.time(14, 5, 7, 270331))),
                ('arrival_time', models.TimeField(default=datetime.time(14, 5, 7, 270386))),
                ('startPrice', models.FloatField(default=0.0)),
                ('endPrice', models.FloatField(default=0.0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]