from django.conf.urls import patterns, url
from bangoo.navigation.menu import views

urlpatterns = patterns('',
    url(r'^$', views.menu, name='admin-menu'),
)