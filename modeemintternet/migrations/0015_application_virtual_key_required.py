# Generated by Django 2.0.1 on 2018-01-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeemintternet', '0014_auto_20180127_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='virtual_key_required',
            field=models.BooleanField(default=False),
        ),
    ]
