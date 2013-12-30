import sys
from django.utils import six
from django import template
from django.conf import settings
from django.template.defaulttags import URLNode
from navigation.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.utils.encoding import smart_text

old_render = URLNode.render

def new_render(self, context):
    """ Override existing url method """
    try:
        ### First: try to find reverse url from static patterns
        return old_render(self, context)
    except NoReverseMatch:
        pass
    act_menu = context.get('act_menu', None)
    args = [arg.resolve(context) for arg in self.args]
    kwargs = dict([(smart_text(k, 'ascii'), v.resolve(context))
                   for k, v in self.kwargs.items()])
    view_name = self.view_name.resolve(context)
    if not view_name:
        raise NoReverseMatch("'url' requires a non-empty first argument. "
            "The syntax changed in Django 1.5, see the docs.")
    url = ''
    try:
        url = reverse(view_name, args=args, kwargs=kwargs, current_app=context.current_app, urlconf=act_menu.urlconf)
    except NoReverseMatch:
        exc_info = sys.exc_info()
        if settings.SETTINGS_MODULE:
            project_name = settings.SETTINGS_MODULE.split('.')[0]
            try:
                url = reverse(project_name + '.' + view_name,
                          args=args, kwargs=kwargs,
                          current_app=context.current_app)
            except NoReverseMatch:
                if self.asvar is None:
                    # Re-raise the original exception, not the one with
                    # the path relative to the project. This makes a
                    # better error message.
                    six.reraise(*exc_info)
        else:
            if self.asvar is None:
                raise

    if self.asvar:
        context[self.asvar] = url
        return ''
    else:
        return url


URLNode.render = new_render


from django.template.loader import add_to_builtins
add_to_builtins('navigation.templatetags.navigation_tags')