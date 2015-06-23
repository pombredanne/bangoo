from os.path import abspath, dirname, join
### BASE_DIR is two levels up to this file
BASE_DIR = dirname(dirname(dirname(abspath(__file__)))).replace('\\','/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sq3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_ROOT = BASE_DIR + '/uploads/'
MEDIA_URL = '/uploads/'
STATIC_ROOT = BASE_DIR + '/static/'
STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'bangoo.theming.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '{{ secret_key }}'

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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bangoo.theming.middleware.ThemeMiddleware',
    'bangoo.navigation.middleware.MenuResolverMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

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
    'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.staticfiles',
    ### Bangoo core modules
    'bangoo.admin', 'bangoo.content', 'bangoo.navigation', 'bangoo.theming', 'bangoo.media',
    ### Bangoo plugins
    ### 3rd-party apps
    'crispy_forms', 'taggit', 'easy_thumbnails'
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
    ('en', 'English'),
)

LOGIN_REDIRECT_URL = '/'

### Theming
THEMES_BASE_DIR = join(dirname(dirname(__file__)), 'themes').replace('\\','/')
THEME = 'default'

THUMBNAIL_ALIASES = {
    'media': {
        'small': {'size': (150, 150), 'quality': 85},
    },
}
THUMBNAIL_SUBDIR = 'thumbs'