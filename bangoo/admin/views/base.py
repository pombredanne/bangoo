from django.shortcuts import render


def home(request, template_name='admin/home.html'):
    #menus = MenuItem.objects.all()
    return render(request, template_name)