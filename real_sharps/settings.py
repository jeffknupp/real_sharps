"""
Django settings for real_sharps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&8lu@-ap3^fz82gun4wxmha%lup0_mt!(-gop+o1=ca+wecq@y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

STATIC_ROOT = '/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cappers',
    'guardian',
    'django_extensions',
    'south',
    'autoslug',
    'sorl.thumbnail',
    'djstripe',
    'allauth',
    'allauth.account',
    'debug_toolbar',
    'crispy_forms',
    'pybb',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'djstripe.context_processors.djstripe_settings',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'pybb.context_processors.processor',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    'guardian.backends.ObjectPermissionBackend',
)

TEMPLATE_DIRS = ('templates/', )
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djstripe.middleware.SubscriptionPaymentMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'real_sharps.urls'

WSGI_APPLICATION = 'real_sharps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'application',
        'USER': 'jknupp',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django-Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ACCOUNT_PASSWORD_MIN_LENGTH = 1

# Django-Crispy-Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

ANONYMOUS_USER_ID = -1

# DJ-Stripe settings

DJSTRIPE_PLANS = {
    "monthly": {
        "stripe_plan_id": "pro-monthly",
        "name": "RealSharpLounge Pro Monthly ($40/month)",
        "description": "The monthly subscription plan to RealSharpLounge",
        "price": 4000,  # $25.00
        "currency": "usd",
        "interval": "month",
        #"image": "/static/lounge.jpg",
    },
    "yearly": {
        "stripe_plan_id": "pro-yearly",
        "name": "RealSharpLounge Pro Yearly ($365/year)",
        "description": "The annual subscription plan to RealSharpLounge",
        "price": 36500,  # $19900
        "currency": "usd",
        "interval": "year",
        #"image": "/static/lounge.jpg",
    }
}

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_w3qNBkDR8A4jkKejBmsMdH34")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_VXxFQI4v3Ym2EwnXh79mzDoN")

DJSTRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = (
    'home',
    'account_logout',  # anything in the django-allauth URLConf
)
