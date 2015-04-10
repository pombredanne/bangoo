# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('experience', models.CharField(choices=[('expert', 'Expert'), ('begin', 'Beginner'), ('inter', 'Intermediate')], max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_page', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('published', models.DateTimeField(verbose_name='published', blank=True, null=True)),
                ('allow_comments', models.BooleanField(default=False, verbose_name='allow comments')),
                ('template_name', models.CharField(help_text="Example: 'content/contact_page.html'. If this isn't provided, the system will use 'content/default.html'.", verbose_name='template name', blank=True, max_length=70)),
                ('registration_required', models.BooleanField(default=False, verbose_name='registration required')),
                ('authors', models.ManyToManyField(verbose_name='authors', to='content.Author')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('url', models.CharField(verbose_name='url', max_length=255)),
                ('text', models.TextField(verbose_name='content', blank=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(to='content.Content', related_name='translations', editable=False, null=True)),
            ],
            options={
                'permissions': (('Can list all content', 'list_contents'),),
                'abstract': False,
                'db_table': 'content_content_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('url', 'language_code'), ('language_code', 'master')]),
        ),
    ]
