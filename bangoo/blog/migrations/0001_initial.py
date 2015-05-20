# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='blog_author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(to='blog.Author')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
    ]
