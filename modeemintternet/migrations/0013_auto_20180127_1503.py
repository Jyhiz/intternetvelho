# Generated by Django 2.0.1 on 2018-01-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeemintternet', '0012_auto_20171204_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='text',
        ),
    ]
