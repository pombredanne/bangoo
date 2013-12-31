# Django settings for examplesite project.
from os.path import abspath, dirname, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Demo admin', 'demo@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sq3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Budapest'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Directories
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__)))).replace('\\','/')
MEDIA_ROOT = PROJECT_ROOT + '/uploads/'
MEDIA_URL = '/uploads/'
STATIC_ROOT = PROJECT_ROOT + '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ("site_media", join(dirname(dirname(__file__)),'site_media').replace('\\','/')),
    ("themes", join(dirname(dirname(__file__)),'themes').replace('\\','/')),
)

STATICFILES_FINDERS = (
    'bangoo.theming.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'sa6w$81l8c#tmno44f(9iv1^#awxvx7g_wy(iv2#87!@fp&^&#'

TEMPLATE_LOADERS = (
    'bangoo.theming.loaders.themes.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'bangoo.theming.middleware.ThemeMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bangoo.navigation.middleware.MenuResolverMiddleware',
)

ROOT_URLCONF = 'examplesite.urls'

WSGI_APPLICATION = 'examplesite.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'bangoo.theming.context_processors.act_theme',
    'bangoo.navigation.context_processors.act_menu',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ### Bangoo core modules
    'bangoo.admin',
    'bangoo.content',
    'bangoo.navigation',
    'bangoo.theming',
    'bangoo.media',
    ### 3rd-party apps
    'crispy_forms',
    'taggit',
    'richforms',
    'ajaxtables',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

ALLOWED_HOSTS = []
CRISPY_TEMPLATE_PACK = 'bootstrap3'
LANGUAGES = (
    ('en', u'English'),
    ('hu', u'Hungarian'),
)

LOGIN_REDIRECT_URL = '/admin/'

### Theming
THEMES_BASE_DIR = join(dirname(dirname(__file__)), 'themes').replace('\\','/')
THEME = 'default'
