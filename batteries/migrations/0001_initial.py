# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('max_volts', models.DecimalField(max_digits=7, verbose_name='Max voltage, V', decimal_places=4)),
                ('min_volts', models.DecimalField(max_digits=7, verbose_name='Min voltage, V', decimal_places=4)),
                ('capacity', models.DecimalField(max_digits=7, verbose_name='standard capacity, Ah', decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='BatteryState',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='state timestamp')),
                ('voltage', models.DecimalField(max_digits=7, verbose_name='measured voltage, V', decimal_places=4)),
                ('capacity_state', models.DecimalField(max_digits=5, verbose_name='Percent capacity', decimal_places=4)),
                ('battery', models.ForeignKey(to='batteries.Battery')),
            ],
        ),
    ]
