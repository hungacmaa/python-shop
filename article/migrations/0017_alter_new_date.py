# Generated by Django 3.2.7 on 2021-11-18 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_alter_new_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 13, 46, 3, 105580)),
        ),
    ]
