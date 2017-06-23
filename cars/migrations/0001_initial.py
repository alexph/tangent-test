# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('Volvo', 'Volvo'), ('BMW', 'BMW'), ('Ford', 'Ford'), ('Mercedes', 'Mercedes'), ('Aston Martin', 'Aston Martin')], max_length=50)),
                ('manufacture_date', models.DateField()),
                ('colour', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('orange', 'orange'), ('purple', 'purple')], max_length=25)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fuel_efficiency_rating', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('has_ejector_seat', models.BooleanField(default=False)),
            ],
        ),
    ]
