# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anothercrm', '0003_auto_20150526_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='relationships',
        ),
        migrations.AddField(
            model_name='relationship',
            name='person',
            field=models.ForeignKey(default=1, to='anothercrm.Person'),
            preserve_default=False,
        ),
    ]
