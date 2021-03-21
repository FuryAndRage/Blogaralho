"""
Django settings for blogaralho project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'si0lzxi_wx^3czoy5y$@m4&1f@-u8(j94n5y9b_!bvsx!f0*^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Third party apps
    'webpack_loader',
    'corsheaders',
    'django_summernote',
    'rest_framework',

    # Our own apps
    'blogaralho.apps.core',
    'blogaralho.apps.categories',
    'blogaralho.apps.posts',
    


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #Third party middlewares
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'blogaralho.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogaralho.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'
# Definindo aqui onde os arquivos estaticos serao servidos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build"),
]

# configuracao adicional para o webpack_loader
WEBPACK_LOADER = {
    'MANIFEST_FILE': os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}

# Variaveis de configuracao para inclusao de cabecalho CORS
CSRF_COOKIE_NAME = "XSRF-TOKEN"
CORS_ORIGIN_ALLOW_ALL = True   

CORS_ORIGIN_WHITELIST = [
'http://localhost:8000',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICANTION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.IsAdminUser', ),
}
