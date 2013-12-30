from django.conf.urls import url, patterns
from navigation import views

urlpatterns = patterns('',
    url(r'', views.menu_dispatcher),
)