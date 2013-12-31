from .forms import CustomAuthenticationForm
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

### Static url patterns; these urls aren't handled by navigation system
static_patterns = patterns('',
    url(r'^admin/', include('bangoo.admin.urls')),
    url(r'^media/', include('bangoo.media.urls')),
    url(r'^accounts/login/$', auth_views.login, {'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^accounts/change_password/$', auth_views.password_change, {'post_change_redirect' : '/accounts/change_password/done/'}, name='change-password'),
    url(r'^accounts/change_password/done/$', auth_views.password_change_done),
    url(r'^accounts/reset_password/$', auth_views.password_reset, name='password-reset'),
    url(r'^accounts/reset_password/done/$', auth_views.password_reset_done),
    url(r'^accounts/reset_password/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm), 
    url(r'^accounts/reset_password/complete/$', auth_views.password_reset_complete),
)
### If we are in DEBUG mode, then handle static files also
if settings.DEBUG:
    static_patterns += staticfiles_urlpatterns()
    static_patterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT})
    )

### Any other urls handled by the manu system.
menu_patterns = i18n_patterns('',
    url(r'', include('bangoo.navigation.urls')),
)

### Concatenate url configs
urlpatterns = static_patterns + menu_patterns
