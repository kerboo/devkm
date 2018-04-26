# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-20 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
