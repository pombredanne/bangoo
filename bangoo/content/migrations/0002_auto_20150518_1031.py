# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='experience',
            field=models.CharField(choices=[('begin', 'Beginner'), ('inter', 'Intermediate'), ('expert', 'Expert')], max_length=10),
            preserve_default=True,
        ),
    ]
