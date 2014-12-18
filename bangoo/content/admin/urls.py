from . import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.ContentList.as_view(), name='admin-content-list'),
    #url(r'^$', views.edit_content, name='admin-content-edit'),
    url(r'^(?P<content_id>\d+)/edit/$', views.edit_content, name='admin-content-edit')
)