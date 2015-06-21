# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('experience', models.SmallIntegerField(max_length=10, verbose_name='experience', choices=[(1, 'beginner'), (2, 'intermediate'), (3, 'expert')])),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('nickname', models.CharField(blank=True, null=True, verbose_name='nickname', max_length=20)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into bangoo admin site', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
