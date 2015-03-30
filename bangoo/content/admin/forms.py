#encoding: utf8
from crispy_forms.bootstrap import FormActions, Accordion, AccordionGroup
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from richforms import widgets
from richforms.fields import TagItField
from taggit.models import Tag

from bangoo.content.models import Content, Author


class EditContentForm(forms.ModelForm):
    #authors = forms.ModelMultipleChoiceField(queryset=Author.objects.filter(user__is_active=True), help_text='',
    #                                         widget=widgets.SelectMupltipleWithCheckbox(widget_attrs={'filter': "true", "width": "800"}))

    class Meta:
        model = Content
        fields = ['authors', 'allow_comments', 'template_name', 'registration_required', 'is_page']
    
    def __init__(self, *args, **kwargs):
        self.base_fields['authors'].help_text = ''
        self.base_fields['authors'].widget.attrs['style'] = 'width: 100%'
        super(EditContentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        a = Accordion()
        self.helper.layout.fields.append(a)
        for lang_code, lang in settings.LANGUAGES:
            required = True if lang_code == settings.LANGUAGE_CODE.split('-')[-1] else False
            self.fields['title_%s' % lang_code] = forms.CharField(max_length=200, label='Title (%s)' % lang, required=required)
            self.fields['text_%s' % lang_code] = forms.CharField(required=required, label='Content (%s)' % lang, 
                                                                    widget=forms.Textarea)
            if self.instance.pk:
                try:
                    trans = self.instance.translations.get(language_code=lang_code)
                    self.fields['title_%s' % lang_code].initial = trans.title
                    self.fields['text_%s' % lang_code].initial = trans.text
                except:
                    pass
            ag = AccordionGroup( _('Text in %(language)s' % {'language': lang.lower()}), 
                                 'title_%s' % lang_code, 'text_%s' % lang_code )
            a.fields.append(ag)
        p = AccordionGroup(_('Page settings'), 'authors', 'allow_comments', 'template_name', 'registration_required',
                            'is_page', css_class="form-panel")
        self.helper.layout.fields.append(p)
        self.helper.layout.append(FormActions(Submit('submit', 'Ment', css_class='btn-primary')))

    def clean(self, *args, **kwargs):
        data = super(EditContentForm, self).clean(*args, **kwargs)
        if 'authors' not in data:
            raise ValidationError(_(u"Author is not set. Check 'Page settings'"))
        if not self.is_valid():
            return data
        data['page_texts'] = []
        for lang_code, lang in settings.LANGUAGES:
            title = data['title_%s' % lang_code]
            text = data['text_%s' % lang_code]
            if all([len(title), len(text)]):
                p = {'language_code': lang_code, 'title': title, 'text': text}
                ###if it's a widget, then make the url unique with language code
                if not data['is_page']:
                    p['url'] += '%s/' % lang_code
                data['page_texts'].append(p)
        return data

    def save(self, *args, **kwargs):
        obj = super(EditContentForm, self).save(*args, **kwargs)
        #obj.translations.all().delete()
        for pt in self.cleaned_data['page_texts']:
            tr = Content.objects.language(pt['language_code']).get(pk=obj.pk)
            tr.text = pt['text']
            #obj.translate(pt['language_code'])
            #for label in pt.keys():
            #    if label in ('language_code', 'url'):
            #        continue
            #    setattr(obj, label, pt[label])
            tr.save()
        return obj
