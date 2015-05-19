# coding: utf-8

import json

from django.core.urlresolvers import reverse
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from restify import status
from restify.http.response import ApiResponse
from restify.resource import ModelResource
from restify.serializers import ModelSerializer

from bangoo.blog.admin.forms import PostForm, PostPublishForm
from bangoo.blog.models import Post


class PostSerializer(ModelSerializer):
    def flatten(self, data):
        if isinstance(data, QuerySet):
            posts = []
            for post in data:
                posts.append({
                    'id': post.pk,
                    'title': post.title,
                    'created_at': post.created_at,
                    'published_at': post.published_at,
                    'endpoint': reverse('edit', urlconf='bangoo.blog.admin.urls', args=[post.pk], prefix='')
                })
            return posts
        elif hasattr(data, 'instance') and data.instance.pk:
            reply = super(PostSerializer, self).flatten(data.instance)
            reply['url'] = reverse('api:post-api', args=[data.instance.pk])
            reply['endpoint'] = reverse('edit', urlconf='bangoo.blog.admin.urls', args=[data.instance.pk], prefix='')
            return reply
        else:
            return super(PostSerializer, self).flatten(data)


class PostResource(ModelResource):
    class Meta:
        resource_name = 'post-api'
        serializer = PostSerializer

    def get(self, request, post_id):
        if post_id == 'list':
            posts = Post.objects.filter(author=request.user.blog_author).all()
            return ApiResponse(posts)
        elif post_id == 'new':
            form = PostForm()
            return ApiResponse(form)
        else:
            post = get_object_or_404(Post, pk=post_id, author=request.user.blog_author)
            return ApiResponse(post)

    def post(self, request, post_id):
        post = json.loads(request.body.decode())

        if post_id == 'new':
            instance = Post()
            instance.author = request.user.blog_author
        elif post_id == 'publish':
            instance = get_object_or_404(Post, pk=post['id'], author=request.user.blog_author)
        else:
            instance = get_object_or_404(Post, pk=post_id, author=request.user.blog_author)

        if post_id == 'publish':
            form = PostPublishForm(post, instance=instance)
        else:
            form = PostForm(post, instance=instance)

        if form.is_valid():
            form.save()
            return ApiResponse(form)
        else:
            return ApiResponse(form.errors, status_code=status.HTTP_400_BAD_REQUEST)
