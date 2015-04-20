# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0002_auto_20150418_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Published', default=datetime.datetime(2015, 4, 18, 19, 49, 23, 411468, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
