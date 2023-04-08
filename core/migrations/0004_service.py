# Generated by Django 3.2.7 on 2021-11-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211112_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('web_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('map', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('youtube', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('open_time', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
