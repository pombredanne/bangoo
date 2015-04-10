from django.utils import timezone
from bangoo.content.models import Content


def menu_created_callback(sender, **kwargs):
    menu = kwargs['menu']
    if menu.plugin != 'bangoo.content':
        return

    content = Content.objects.create(published=timezone.now())
    for trans in menu.translations.all():
        content.translate(trans.language_code)
        content.title = menu.title
        content.url = menu.path
        content.text = ''
        content.save()