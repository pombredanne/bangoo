from django.conf.urls import patterns, url
from bangoo.content.menu import views

urlpatterns = patterns('',
    url(r'^$', views.menu, name='admin-menu'),
)