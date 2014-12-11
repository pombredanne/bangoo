from django.conf.urls import url, patterns, include
from . import views
#from content import admin as content_admin


urlpatterns = patterns('',
    url(r'^$', views.home, name='admin-home'),

    url(r'^menu/$', include('bangoo.content.menu.urls')),
    url(r'^content/', include('bangoo.content.admin.urls')),
)