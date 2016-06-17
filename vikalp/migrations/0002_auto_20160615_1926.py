# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vikalp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ctc',
            field=models.CharField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='company',
            name='experience',
            field=models.CharField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
