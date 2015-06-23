from django.shortcuts import render
from bangoo.navigation.utils import get_urlconf
from django.core.urlresolvers import resolve


def home(request, template_name='admin/home.html'):
    return render(request, template_name)


def admin_menu_dispatcher(request, menu_id):
    uconf = get_urlconf(request.act_menu.plugin, frontend_urls=False)

    prefix = '/admin/menu/%s' % menu_id  # TODO: szebb megoldast
    func, args, kwargs = resolve(request.path[len(prefix):], urlconf=uconf)
    return func(request, *args, **kwargs)
