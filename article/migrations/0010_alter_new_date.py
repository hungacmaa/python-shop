# Generated by Django 3.2.7 on 2021-11-17 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_new_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 17, 18, 58, 49, 488280)),
        ),
    ]