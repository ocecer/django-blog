# Generated by Django 4.0.6 on 2022-08-01 11:01

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, verbose_name='categoryName')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]