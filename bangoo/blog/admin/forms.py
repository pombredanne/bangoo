# coding: utf-8

from django import forms

from bangoo.blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')  # , 'tags')
