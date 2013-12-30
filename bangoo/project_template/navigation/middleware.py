from django.http import Http404
from navigation.models import Menu
from navigation.views import menu_dispatcher


class MenuResolverMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Firstly we have to check which view function has to be called. If the view is 'menu_dispatcher' function,
        then find the actual menu according to request.path. If no menu can be found, then raise 404 error.

        If the view isn't 'menu_dispatcher', then it's a 'static' function (defined in project urls.py). 
        > No menu has to be found.
        """
        if view_func != menu_dispatcher:
            return None ## It's a static url, nothing to do.
        path = request.path[1:].strip(request.LANGUAGE_CODE)
        parts = path.strip('/').split('/')
        ### Order by menu level desc, mean try to find the actual menu on the most deep level
        menus = Menu.objects.language(request.LANGUAGE_CODE)\
                            .filter(path__startswith='/' + parts[0]).order_by('-level')
        for menu in menus:
            if path.startswith(menu.path):
                request.act_menu = menu
                return None
        raise Http404()