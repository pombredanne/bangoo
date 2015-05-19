# coding: utf-8

from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='blog_author')

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    author = models.ForeignKey(Author)

    title = models.CharField(max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_at']
