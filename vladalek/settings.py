import os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

SECRET_KEY = os.environ['secret']

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'tinymce',
    'blog.apps.BlogConfig',
    'home.apps.HomeConfig',
]

TINYMCE_DEFAULT_CONFIG = {
	'height': 360,
	'width': 750,
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 20,
	'plugins': '''
	textcolor save link image media preview codesample contextmenu
	table code lists fullscreen insertdatetime nonbreaking
	contextmenu directionality searchreplace wordcount visualblocks
	visualchars code fullscreen autolink lists charmap print hr
	anchor pagebreak
	''',
	'toolbar1': '''
	fullscreen preview bold italic underline | fontselect,
	fontsizeselect | forecolor backcolor | alignleft alignright |
	aligncenter alignjustify | indent outdent | bullist numlist table |
	| link image media | codesample |
	''',
	'toolbar2': '''
	visualblocks visualchars |
	charmap hr pagebreak nonbreaking anchor | code |
	''',
	'contextmenu': 'formats | link image',
	'menubar': True,
	'statusbar': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vladalek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        	os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
            	'pagination_tags': 'vladalek.templatetags.pagination_tags',
            },
        },
    },
]

WSGI_APPLICATION = 'vladalek.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticroot')
STATICFILES_DIRS = [
	os.path.join(PROJECT_ROOT, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

