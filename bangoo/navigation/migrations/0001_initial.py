# -*- coding: utf-8 -*-


from django.db import models, migrations
import jsonfield.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_required', models.BooleanField(default=False)),
                ('urlconf', models.CharField(max_length=100, null=True, blank=True)),
                ('weight', models.SmallIntegerField(default=0)),
                ('parameters', jsonfield.fields.JSONField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='navigation.Menu', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='navigation.Menu', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'navigation_menu_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='menutranslation',
            unique_together=set([('language_code', 'master'), ('path', 'language_code')]),
        ),
    ]
