from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from bangoo.navigation.models import Menu


@permission_required('menu.list_menu')
def menu(request, template_name='content/menu/menu.html'):
    return render(request, template_name, {'nodes': Menu.objects.all()})