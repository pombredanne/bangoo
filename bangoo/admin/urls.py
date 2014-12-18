from django.conf.urls import url, patterns, include
from . import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='admin-home'),
    url(r'^menu/', include('bangoo.navigation.menu.urls')),
    url(r'^menu/(?P<menu_id>\d+)/edit/', views.admin_menu_dispatcher, name='edit-menu'),
    url(r'^content/', include('bangoo.content.admin.urls')),
)