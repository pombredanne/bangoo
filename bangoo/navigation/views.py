from .models import Menu
from django.core.urlresolvers import resolve
from django.http import Http404
from django.shortcuts import render


def menu_dispatcher(request):
    path = request.path[1:].strip(request.LANGUAGE_CODE)
    func, args, kwargs = resolve(path[len(request.act_menu.path) - 1:], urlconf=request.act_menu.urlconf)
    return func(request, *args, **kwargs)