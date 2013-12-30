# encoding: utf8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translations import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-signin'
        self.helper.form_style = 'inline'
        self.helper.help_text_inline = True
        self.helper.label_class = ''
        self.helper.add_input(Submit('login', 'Login', css_class='btn btn-lg btn-primary btn-block'))
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML('<h2 class="form-signin-heading">%s</h2>' % _('Please sign in')),
            Field('username', placeholder='Username'),
            Field('password', placeholder='Password'),
        )
