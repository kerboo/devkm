# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='\u90ae\u7bb1')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('is_active', models.BooleanField(default=True, help_text=b'\xe8\xae\xbe\xe7\xbd\xae\xe7\x94\xa8\xe6\x88\xb7\xe7\x8a\xb6\xe6\x80\x81', verbose_name='\u6fc0\u6d3b\u7528\u6237')),
                ('is_staff', models.BooleanField(default=False, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe7\xae\xa1\xe7\x90\x86\xe7\xab\x99\xe7\x82\xb9', verbose_name='\u7ba1\u7406\u7ad9\u70b9')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='\u59d3\u540d')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'myusers',
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u7ba1\u7406',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History_Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(auto_now=True)),
                ('request_method', models.CharField(max_length=12, null=True)),
                ('request_url', models.CharField(max_length=100, null=True)),
                ('user_ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u767b\u5f55\u5386\u53f2',
                'verbose_name_plural': '\u767b\u5f55\u5386\u53f2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'db_table': 'mygroups',
                'verbose_name': '\u7528\u6237\u7ec4',
                'verbose_name_plural': '\u7528\u6237\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Opuser', models.CharField(max_length=12, null=True)),
                ('Optime', models.DateTimeField(auto_now_add=True)),
                ('Opaction', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': '\u64cd\u4f5c\u8bb0\u5f55',
                'verbose_name_plural': '\u64cd\u4f5c\u8bb0\u5f55',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='myusers',
            name='group',
            field=models.ForeignKey(verbose_name='\u5c5e\u7ec4', blank=True, to='accounts.MyGroups', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myusers',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myusers',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
