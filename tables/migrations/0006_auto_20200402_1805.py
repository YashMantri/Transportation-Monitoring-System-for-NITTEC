# Generated by Django 3.0.4 on 2020-04-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_auto_20200401_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operators',
            old_name='operators',
            new_name='name',
        ),
        migrations.AddField(
            model_name='operators',
            name='password',
            field=models.CharField(db_column='password', default='nittec', max_length=10),
        ),
        migrations.AddField(
            model_name='operators',
            name='username',
            field=models.CharField(db_column='username', default='nittec', max_length=20),
        ),
    ]
