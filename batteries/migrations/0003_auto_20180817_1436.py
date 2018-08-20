# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0002_auto_20180817_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterystate',
            name='capacity_state',
            field=models.DecimalField(verbose_name='Percent capacity', decimal_places=4, default=1, max_digits=5),
        ),
    ]
