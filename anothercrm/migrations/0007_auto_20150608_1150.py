# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anothercrm', '0006_auto_20150608_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='trade',
            new_name='trades',
        ),
    ]
