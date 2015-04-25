# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0010_auto_20150425_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 18, 26, 10, 86594, tzinfo=utc), verbose_name='Date Published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 18, 26, 20, 963216, tzinfo=utc), verbose_name='Date Published'),
            preserve_default=False,
        ),
    ]
