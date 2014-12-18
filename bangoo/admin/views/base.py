from django.shortcuts import render
from bangoo.navigation.models import Menu
from django.conf import settings
from django.shortcuts import get_object_or_404
from bangoo.navigation.utils import get_urlconf
from django.core.urlresolvers import resolve


def home(request, template_name='admin/home.html'):
    #menus = MenuItem.objects.all()
    return render(request, template_name)


def admin_menu_dispatcher(request, menu_id):
    lang = settings.LANGUAGES[0][0] ##default language
    menu = get_object_or_404(Menu.objects.language(lang), pk=menu_id)
    uconf = get_urlconf(menu.plugin, frontend_urls=False)
    prefix = '/admin/menu/%s/edit/' % menu_id ##TODO: szebb megoldast
    path = request.path.strip(prefix)
    if not len(path): path = '/'
    func, args, kwargs = resolve(path, urlconf=uconf)
    request.act_menu = menu
    return func(request, *args, **kwargs)
