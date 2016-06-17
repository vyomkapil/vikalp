# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vikalp', '0004_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='title',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
