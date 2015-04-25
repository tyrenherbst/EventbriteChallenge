# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0011_auto_20150425_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 19, 36, 38, 70420, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 19, 36, 38, 69420, tzinfo=utc), verbose_name='Date Published'),
        ),
    ]
