from django import template
from django.forms import Select
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def bootstrap_field(field, model, errors):
    widget = field.field.widget.__class__.__name__
    attrs = {
        'field': field,
        'widget': widget,
        'model': model,
        'errors': errors
    }

    if isinstance(field.field.widget, Select):
        attrs['choices'] = field.field.choices

    r = render_to_string('angular/bs_field.html', attrs)
    return r


@register.simple_tag
def redactor_field(field, model, errors):
    widget = field.field.widget.__class__.__name__
    attrs = {
        'field': field,
        'widget': widget,
        'model': model,
        'errors': errors
    }

    r = render_to_string('angular/redactor_field.html', attrs)
    return r

@register.simple_tag
def bs_form_fields(form, angular_model, angular_errors):
    for field in form:
        setattr(form.fields[field.name], 'angular_model', '{0}.{1}'.format(angular_model, field.name))
        setattr(form.fields[field.name], 'angular_errors', '{0}.{1}'.format(angular_errors, field.name))
    return render_to_string('angular/bs_form_fields.html', {'form': form})