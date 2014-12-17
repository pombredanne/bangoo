from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from bangoo.navigation.models import Menu


class MenuOrderForm(forms.Form):
    METHOD_CHOCES = (
        ('insert', 'Insert'),
        ('move', 'Move')
    )

    method = forms.ChoiceField(choices=METHOD_CHOCES)
    source = forms.IntegerField()
    target = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(MenuOrderForm, self).__init__(*args, **kwargs)

        self.default_locale = settings.LANGUAGE_CODE.split('-')[0]

    def clean_target(self):
        try:
            target_id = self.cleaned_data['target']
            target_menu = Menu.handler.language(self.default_locale).get(id=target_id)

            return target_menu
        except Menu.DoesNotExist:
            raise ValidationError(_('Menu does not exist'))

    def clean_source(self):
        try:
            which_id = self.cleaned_data['source']
            which_menu = Menu.handler.language(self.default_locale).get(id=which_id)

            return which_menu
        except Menu.DoesNotExist:
            raise ValidationError(_('Menu does not exist'))