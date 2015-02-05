# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience', models.CharField(max_length=10, choices=[(b'begin', b'Beginner'), (b'inter', b'Itermediate'), (b'expert', b'Expert')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_page', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('published', models.DateTimeField(null=True, verbose_name='published', blank=True)),
                ('allow_comments', models.BooleanField(default=False, verbose_name='allow comments')),
                ('template_name', models.CharField(help_text="Example: 'content/contact_page.html'. If this isn't provided, the system will use 'content/default.html'.", max_length=70, verbose_name='template name', blank=True)),
                ('registration_required', models.BooleanField(default=False, verbose_name='registration required')),
                ('authors', models.ManyToManyField(to='content.Author', verbose_name='authors')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('url', models.CharField(unique=True, max_length=255, verbose_name='url')),
                ('text', models.TextField(null=True, verbose_name='content', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='content.Content', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'content_content_translation',
                'permissions': (('Can list all content', 'list_contents'),),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
