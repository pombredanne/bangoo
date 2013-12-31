from . import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^redactor/images/list/$', views.list_images, name='media-redactor-list-images'),
    url(r'^redactor/images/upload/$', views.upload_images, name='media-redactor-upload-images'),
)