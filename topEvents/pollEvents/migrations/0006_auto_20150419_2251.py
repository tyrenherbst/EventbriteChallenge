# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollEvents', '0005_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='results',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='results',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='results',
            name='eID',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='results',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
