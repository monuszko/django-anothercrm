# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anothercrm', '0002_auto_20150526_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='relationships',
            field=models.ManyToManyField(to='anothercrm.Relationship', blank=True),
        ),
    ]
