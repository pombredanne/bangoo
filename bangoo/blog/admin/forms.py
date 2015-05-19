# coding: utf-8

from datetime import datetime

from django import forms

from bangoo.blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')  # , 'tags')

    def __init__(self, post=None, **kwargs):
        if post:
            self.post_state = post.pop('state')
        super(PostForm, self).__init__(post, **kwargs)

    def save(self, commit=True):
        if self.post_state == 'publish':
            self.instance.published_at = datetime.now()
        elif self.post_state == 'draft':
            self.instance.published_at = None
        return super(PostForm, self).save(commit)


class PostPublishForm(forms.Form):
    state = forms.ChoiceField(
        choices=(
            ('publish', None),
            ('draft', None)
        )
    )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super(PostPublishForm, self).__init__(*args, **kwargs)

    def save(self):
        if self.cleaned_data['state'] == 'publish':
            self.instance.published_at = datetime.now()
        else:
            self.instance.published_at = None
        self.instance.save()
        return self.instance