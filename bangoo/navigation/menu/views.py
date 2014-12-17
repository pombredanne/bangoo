import json
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render

from bangoo.navigation.menu.forms import MenuOrderForm
from bangoo.navigation.models import Menu

from signals import menu_changed

"""
@receiver(menu_changed)
def menu_changed_handler(**kwargs):
    sender = kwargs['sender']
    menu = kwargs['menu']
    old_parent = kwargs['old_parent']
    new_parent = kwargs['new_parent']

    print '"{0}"\n\tmoved "{1}" from "{2}" to "{3}"'.format(sender,
                                                 menu,
                                                 old_parent,
                                                 new_parent)"""

@permission_required('menu.list_menu')
def menu(request, template_name='navigation/menu/menu.html'):
    return render(request, template_name, {'nodes': Menu.objects.all()})


def create_path(menu, old, new):
    # TODO: This is not so stable
    path = menu.path
    old_path = getattr(old, 'path', '/')
    new_path = getattr(new, 'path', '/')

    if path.startswith(old_path):
        path = path[len(old_path):]
        path = new_path + path
    return path


@permission_required('menu.reorder')
def reorder_menu(request):
    if request.POST:
        form = MenuOrderForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            target_menu = form.cleaned_data['target']
            source_menu = form.cleaned_data['source']

            if method == 'move':
                source_menu_parent = source_menu.parent
                source_menu.move_to(target_menu, position='left')
                source_menu.path = create_path(source_menu, source_menu_parent, target_menu.parent)
                source_menu.save()

                menu_changed.send(sender=reorder_menu,
                                  menu=source_menu,
                                  old_parent=source_menu_parent,
                                  new_parent=target_menu.parent)

            if method == 'insert':
                source_menu_parent = source_menu.parent
                source_menu.move_to(target_menu)
                source_menu.path = create_path(source_menu, source_menu_parent, target_menu)
                source_menu.save()

                menu_changed.send(sender=reorder_menu,
                                  menu=source_menu,
                                  old_parent=source_menu_parent,
                                  new_parent=target_menu)

            return HttpResponse(json.dumps({
                'menu_id': source_menu.id,
                'path': source_menu.path
            }), content_type='application/json')
    return HttpResponse()