from django.shortcuts import render


def menu(request, template_name='content/menu/menu.html'):
    return render(request, template_name)