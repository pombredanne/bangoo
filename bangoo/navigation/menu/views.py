from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render
from bangoo.navigation.menu.forms import MenuOrderForm
from bangoo.navigation.models import Menu


@permission_required('menu.list_menu')
def menu(request, template_name='navigation/menu/menu.html'):
    return render(request, template_name, {'nodes': Menu.objects.all()})

@permission_required('menu.reorder')
def reorder_menu(request):
    if request.POST:
        form = MenuOrderForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            target_menu = form.cleaned_data['target']
            source_menu = form.cleaned_data['source']

            if method == 'move':
                source_menu.move_to(target_menu, position='left')
                source_menu.save()
            if method == 'insert':
                source_menu.move_to(target_menu)
                source_menu.save()

    return HttpResponse()