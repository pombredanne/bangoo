from django.conf.urls import url, patterns, include

import api
from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='admin-home'),
    url(r'^menu/(?P<menu_id>\d+)/', views.admin_menu_dispatcher, name='edit-in-menu'),
    url(r'^menu/', include('bangoo.navigation.menu.urls')),
    url(r'^api/', include(api.api.urls, namespace='api'))
)