# Generated by Django 3.2.7 on 2021-11-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_productimage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vote',
            field=models.IntegerField(default=5),
        ),
    ]