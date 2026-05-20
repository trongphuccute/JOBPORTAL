from pathlib import Path
from pickle import FALSE
from decouple import config
from datetime import timedelta
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY
SECRET_KEY = config('SECRET_KEY')

# DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'accounts',
    'jobs',
    'applications',
    'blog',
    'cloudinary',
    'cloudinary_storage',
    'axes',
    'ai_assistant',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'jobportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.notifications_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'jobportal.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL')
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

BASE_DIR = Path(__file__).resolve().parent.parent

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'

EMAIL_HOST_USER = "apikey"
SENDGRID_API_KEY = config("SENDGRID_API_KEY")

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# Site URL for email templates and links
SITE_URL = config('SITE_URL', default='https://jobportal-4z3o.onrender.com')

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'accounts.utils': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
APPEND_SLASH = True

CLOUDINARY_STORAGE = {
    'cloud_name' : config('CLOUDINARY_CLOUD_NAME'),
    'api_key' : config('CLOUDINARY_API_KEY'),
    'api_secret' : config('CLOUDINARY_API_SECRET')
}
STORAGES = {
    'default':{
        'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AXES_FAILURE_LIMIT = 5

AXES_COOLOFF_TIME = timedelta(minutes=15)

AXES_LOCKOUT_PARAMETERS = ["ip_address"]

AXES_RESET_ON_SUCCESS = True

GEMINI_API_KEY = config('GEMINI_API_KEY')

UNFOLD = {

    "SITE_TITLE": "Job Portal Admin",

    "SITE_HEADER": "Job Portal",

    "SITE_SYMBOL": "work",

}