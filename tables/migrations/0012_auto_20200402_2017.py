# Generated by Django 3.0.4 on 2020-04-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0011_auto_20200402_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingname',
            name='active',
            field=models.NullBooleanField(),
        ),
    ]
