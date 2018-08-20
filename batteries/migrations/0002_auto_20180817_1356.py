# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batterystate',
            name='date',
        ),
        migrations.AddField(
            model_name='batterystate',
            name='timestamp',
            field=models.DateTimeField(verbose_name='state timestamp', default=datetime.datetime(2018, 8, 17, 13, 56, 32, 640133, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
