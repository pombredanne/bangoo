#encoding: utf8
from django.contrib.auth.models import User
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Author(User):
    """
    experience: Level of experience, how complicated edit surface will the author have.
    """
    EXPERIANCE_CHOICES = {
        'begin': 'Beginner',
        'inter': 'Itermediate',
        'expert': 'Expert'
    }
    experience = models.CharField(max_length=10, choices=EXPERIANCE_CHOICES.items())

    def __unicode__(self):
        return self.username

class Content(TranslatableModel):
    is_page = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author, verbose_name=_('authors'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    published = models.DateTimeField(verbose_name=_('published'), blank=True, null=True)
    allow_comments = models.BooleanField(_('allow comments'), default=False)
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'content/contact_page.html'. If this isn't provided, the system will use 'content/default.html'."))
    registration_required = models.BooleanField(_('registration required'), default=False)
    translations = TranslatedFields(
        title = models.CharField(verbose_name=_('title'), max_length=255),
        url = models.CharField(verbose_name=_('url'), max_length=255, unique=True),
        text = models.TextField(verbose_name=_('content'), blank=True, null=True),
        meta = {
            'permissions': (
                    ('Can list all content', 'list_contents'),
                )
        }
    )