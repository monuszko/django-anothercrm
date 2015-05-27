# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anothercrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=1, choices=[(b'E', b'Employee'), (b'C', b'Client')])),
                ('name', models.CharField(max_length=50)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='relationship',
            name='company',
            field=models.ForeignKey(to='anothercrm.Company'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relatype',
            field=models.ForeignKey(to='anothercrm.RelationshipType'),
        ),
        migrations.AddField(
            model_name='person',
            name='relationships',
            field=models.ManyToManyField(to='anothercrm.Relationship'),
        ),
    ]
