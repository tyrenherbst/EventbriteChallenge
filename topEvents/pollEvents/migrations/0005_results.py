# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0004_category_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('eID', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Results',
            },
        ),
    ]
