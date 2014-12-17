from django.conf.urls import url, patterns, include
from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='admin-home'),

    url(r'^menu/', include('bangoo.navigation.menu.urls')),
    url(r'^content/', include('bangoo.content.admin.urls')),
)