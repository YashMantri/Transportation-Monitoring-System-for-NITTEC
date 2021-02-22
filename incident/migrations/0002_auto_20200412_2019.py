# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-12 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentlog',
            name='helplogid',
            field=models.IntegerField(blank=True, db_column='HelpLogID', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='cleartime',
            field=models.DateTimeField(blank=True, db_column='ClearTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='detectiontime',
            field=models.DateTimeField(blank=True, db_column='DetectionTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='id',
            field=models.AutoField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='lanblockcleartime',
            field=models.DateTimeField(blank=True, db_column='LanBlockClearTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='retnormtime',
            field=models.DateTimeField(blank=True, db_column='RetNormTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='scenearrtime',
            field=models.DateTimeField(blank=True, db_column='SceneArrTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='scenedeparttime',
            field=models.DateTimeField(blank=True, db_column='SceneDepartTime', null=True),
        ),
        migrations.AlterField(
            model_name='incidentlog',
            name='verifytime',
            field=models.DateTimeField(blank=True, db_column='VerifyTime', null=True),
        ),
    ]
