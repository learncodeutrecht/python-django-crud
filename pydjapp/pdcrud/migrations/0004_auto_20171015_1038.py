# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdcrud', '0003_auto_20171015_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('urgent', models.BooleanField()),
                ('important', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]