# -*- coding: utf-8 -*-
from django.db import models, migrations


def data_migr(apps, schema_editor):
    Menu = apps.get_model("navigation", "Menu")
    db_alias = schema_editor.connection.alias
    for m in Menu.objects.using(db_alias):
        if m.plugin:
            m.plugin = m.plugin.strip('.urls')
            m.save()


class Migration(migrations.Migration):
    dependencies = [("navigation", "0001_initial")]
    operations = [
        migrations.RenameField('Menu', 'urlconf', 'plugin'),
        migrations.RunPython(data_migr),
    ]