# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-16 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_img', models.ImageField(blank=True, null=True, upload_to='avatar_img')),
            ],
            options={
                'db_table': 'userprofile',
                'managed': False,
            },
        ),
    ]
