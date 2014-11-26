from bangoo.navigation.models import Menu
from django import template
from django.template.loader import render_to_string
from django.template.defaulttags import URLNode
from django.core.urlresolvers import NoReverseMatch, reverse
from django.template.defaulttags import url as django_url
from django.db.models import Q
register = template.Library()

@register.simple_tag(name='menu', takes_context=True)
def generate_menu(context, custom_classes='', template_name='navigation/default.html'):
    lang = context['request'].LANGUAGE_CODE
    items = Menu.objects.language(lang).filter(parent__isnull=True).order_by('-weight')
    if not context.get('request').user.is_authenticated():
        items = items.exclude(login_required=True)
    active = ''
    for item in items:
        if context['request'].path_info.startswith(item.path) and len(item.path) > len(active):
            active = item.path
    return render_to_string(template_name, {'items': items, 'active': active, 'custom_classes': custom_classes},
                            context_instance=context)


class MenuURLNode(URLNode):
    def render(self, context):
        try:
            return super(MenuURLNode, self).render(context)
        except NoReverseMatch as ex:
            act_menu = context.get('act_menu', None)
            if not act_menu:
                raise ex
            prefix = '/%s/%s' % (context.get('LANGUAGE_CODE'), act_menu.path[1:-1])
            url = reverse(self.view_name.resolve(context), args=self.args, kwargs=self.kwargs, urlconf=act_menu.urlconf)
            return prefix + url


@register.tag
def url(parser, token):
    #Just like {% url %} but ads the path of the current menu as prefix.
    node_instance = django_url(parser, token)
    return MenuURLNode(view_name=node_instance.view_name,
                       args=node_instance.args,
                       kwargs=node_instance.kwargs,
                       asvar=node_instance.asvar)