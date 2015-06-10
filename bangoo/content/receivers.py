# coding: utf-8

from django.db import transaction
from django.utils import timezone

from bangoo.content.models import Content


def menu_created_callback(sender, **kwargs):
    menu = kwargs['menu']

    if menu.plugin != 'bangoo.content':
        return

    content = Content.objects.create(published=timezone.now())
    for menu_trans in menu.translations.all():
        author = kwargs['user'].author
        content.translate(menu_trans.language_code)
        content.title = menu_trans.title
        content.url = menu_trans.path
        content.authors.add(author)
        content.text = ''
        content.save()