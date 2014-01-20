from django import forms
from .models import Image
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from richforms import widgets


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['file'].label = ''
        self.fields['file'].widget = widgets.AjaxFileInput(widget_attrs={'url': reverse('media-image-upload')})
        self.fields['tags'].required = False