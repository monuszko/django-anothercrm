# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anothercrm', '0004_auto_20150527_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(help_text='24 Badger Rd., etc.', max_length=100, verbose_name='Address', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(max_length=2, verbose_name='Country', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 22, 11, 0, 635423, tzinfo=utc), verbose_name='Creation Date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='Email address', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Mobile Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='modification_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 22, 11, 13, 253860, tzinfo=utc), verbose_name='Modification Date', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(max_length=100, verbose_name='State', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='zipcode',
            field=models.CharField(help_text="For example, '80-209' in Poland", max_length=10, verbose_name='Postal code', blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relatype',
            field=models.ForeignKey(verbose_name='relationship type', to='anothercrm.RelationshipType'),
        ),
    ]
