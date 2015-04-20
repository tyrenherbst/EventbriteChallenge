# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0003_category_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cID',
            field=models.IntegerField(default=0),
        ),
    ]
