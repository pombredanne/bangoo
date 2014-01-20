from bangoo.navigation.models import Menu
from django import template
from django.template.loader import render_to_string
from django.db.models import Q
register = template.Library()

@register.simple_tag(name='menu', takes_context=True)
def generate_menu(context, custom_classes='', template_name='navigation/default.html'):
    lang = context['request'].LANGUAGE_CODE
    items = Menu.objects.language(lang).all()
    if not context.get('request').user.is_authenticated():
        items = items.exclude(login_required=True)
    active = ''
    for item in items:
        if context['request'].path_info.startswith(item.path) and len(item.path) > len(active):
            active = item.path
    return render_to_string(template_name, {'items': items, 'active': active, 'custom_classes': custom_classes},
                            context_instance=context)

from django.template.defaulttags import url
from bangoo.navigation.templatetags import URLNode
from django.core.urlresolvers import NoReverseMatch
class MenuURLNode(URLNode):
    def render(self, context):
        act_menu = context.get('act_menu', None)
        prefix = act_menu.path[1:-1] if act_menu else ''
        prefix = '/%s/' % context.get('LANGUAGE_CODE') + prefix
        return prefix + super(MenuURLNode, self).render(context)


@register.tag(name='menu_url')
def menu_url(parser, token, node_cls=MenuURLNode):
    """Just like {% url %} but ads the path of the current menu as prefix."""
    node_instance = url(parser, token)
    return node_cls(view_name=node_instance.view_name,
        args=node_instance.args,
        kwargs=node_instance.kwargs,
        asvar=node_instance.asvar)