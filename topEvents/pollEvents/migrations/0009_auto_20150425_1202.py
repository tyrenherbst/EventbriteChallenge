# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0008_auto_20150425_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]
