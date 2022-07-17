"""
Django settings for karrio.server project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import importlib
from pathlib import Path
from decouple import AutoConfig
from datetime import timedelta
from django.urls import reverse_lazy
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "server" / "VERSION", "r") as v:
    VERSION = v.read().strip()


config = AutoConfig(search_path=Path().resolve())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_MODE", default=True, cast=bool)

# custom env
WORK_DIR = config("WORK_DIR", default="")
Path(WORK_DIR).mkdir(parents=True, exist_ok=True)

USE_HTTPS = config("USE_HTTPS", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*").split(",")

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

# HTTPS configuration
if USE_HTTPS is True:
    global SECURE_SSL_REDIRECT
    global SECURE_PROXY_SSL_HEADER
    global SESSION_COOKIE_SECURE
    global SECURE_HSTS_SECONDS
    global SECURE_HSTS_INCLUDE_SUBDOMAINS
    global CSRF_COOKIE_SECURE
    global SECURE_HSTS_PRELOAD

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 1
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True


# karrio packages settings
KARRIO_CONF = [
    app
    for app in [
        {
            "app": "karrio.server.core",
            "module": "karrio.server.core",
            "urls": "karrio.server.core.urls",
        },
        {
            "app": "karrio.server.providers",
            "module": "karrio.server.providers",
            "urls": "karrio.server.providers.urls",
        },
        {
            "app": "karrio.server.tracing",
            "module": "karrio.server.tracing",
        },
        {
            "app": "karrio.server.graph",
            "module": "karrio.server.graph",
            "urls": "karrio.server.graph.urls",
        },
        {
            "app": "karrio.server.proxy",
            "module": "karrio.server.proxy",
            "urls": "karrio.server.proxy.urls",
        },
        {
            "app": "karrio.server.manager",
            "module": "karrio.server.manager",
            "urls": "karrio.server.manager.urls",
        },
        {
            "app": "karrio.server.events",
            "module": "karrio.server.events",
            "urls": "karrio.server.events.urls",
        },
        {
            "app": "karrio.server.documents",
            "module": "karrio.server.documents",
            "urls": "karrio.server.documents.urls",
        },
        {
            "app": "karrio.server.data",
            "module": "karrio.server.data",
            "urls": "karrio.server.data.urls",
        },
        {"app": "karrio.server.pricing", "module": "karrio.server.pricing"},
        {"app": "karrio.server.apps", "module": "karrio.server.apps"},
    ]
    if importlib.util.find_spec(app["module"]) is not None  # type:ignore
]

KARRIO_APPS = [cfg["app"] for cfg in KARRIO_CONF]
KARRIO_URLS = [cfg["urls"] for cfg in KARRIO_CONF if "urls" in cfg]

ALLOW_ADMIN_APPROVED_SIGNUP = config(
    "ALLOW_ADMIN_APPROVED_SIGNUP", default=False, cast=bool
)
ALLOW_SIGNUP = (
    config("ALLOW_SIGNUP", default=False, cast=bool) or ALLOW_ADMIN_APPROVED_SIGNUP
)
MULTI_ORGANIZATIONS = (
    importlib.util.find_spec("karrio.server.orgs") is not None  # type:ignore
)
ALLOW_MULTI_ACCOUNT = MULTI_ORGANIZATIONS
ORDERS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.orders") is not None  # type:ignore
)
APPS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.apps") is not None  # type:ignore
)
DOCUMENTS_MANAGEMENT = (
    importlib.util.find_spec("karrio.server.documents") is not None  # type:ignore
)
DATA_IMPORT_EXPORT = (
    importlib.util.find_spec("karrio.server.data") is not None  # type:ignore
)
CUSTOM_CARRIER_DEFINITION = (
    importlib.util.find_spec("karrio.mappers.generic") is not None  # type:ignore
)
MULTI_TENANTS = importlib.util.find_spec(  # type:ignore
    "karrio.server.tenants"
) is not None and config("MULTI_TENANT_ENABLE", default=False, cast=bool)


# components path settings
BASE_PATH = config("BASE_PATH", default="")
if len(BASE_PATH) > 0 and BASE_PATH.startswith("/"):
    BASE_PATH = BASE_PATH[1:]
if len(BASE_PATH) > 0 and not BASE_PATH.endswith("/"):
    BASE_PATH = BASE_PATH + "/"

ROOT_URLCONF = "karrio.server.urls"
LOGIN_URL = BASE_PATH + "/login/"
LOGOUT_REDIRECT_URL = BASE_PATH + "/login/"
LOGIN_REDIRECT_URL = BASE_PATH + "/admin/"
OPEN_API_PATH = "openapi/"

NAMESPACED_URLS = [
    ("api/", "rest_framework.urls", "rest_framework"),
]

BASE_APPS = [
    "karrio.server.user",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
]

OTP_APPS = [
    "django_filters",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_email",
    "two_factor",
    "two_factor.plugins.email",
]

INSTALLED_APPS = [
    "constance",
    *KARRIO_APPS,
    *BASE_APPS,
    "rest_framework",
    "django_email_verification",
    "rest_framework_tracking",
    "drf_yasg",
    "constance.backends.database",
    "huey.contrib.djhuey",
    "corsheaders",
    *OTP_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "karrio.server.core.authentication.AuthenticationMiddleware",
    "karrio.server.core.authentication.TwoFactorAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "karrio.server.core.middleware.SessionContext",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "server" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "karrio.server.core.context_processors.get_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "karrio.server.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Karrio Middleware
# KARRIO_ENTITY_ACCESS_METHOD = 'karrio.server.core.middleware.CreatorAccess'
# KARRIO_ENTITY_ACCESS_METHOD = 'karrio.server.core.middleware.WideAccess'
MODEL_TRANSFORMERS: list = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DB_ENGINE = config("DATABASE_ENGINE", default="postgresql_psycopg2")

DATABASES = {
    "default": {
        "NAME": config("DATABASE_NAME", default="db"),
        "ENGINE": "django.db.backends.{}".format(DB_ENGINE),
        "PASSWORD": config("DATABASE_PASSWORD", default="postgres"),
        "USER": config("DATABASE_USERNAME", default="postgres"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("DATABASE_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = "user.User"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = config("STATIC_URL", default=f"{BASE_PATH}/static/".replace("//", "/"))
STATIC_ROOT = config("STATIC_ROOT_DIR", default=(BASE_DIR / "server" / "staticfiles"))

STATICFILES_DIRS = [
    BASE_DIR / "server" / "static" / "karrio",
    BASE_DIR / "server" / "static" / "extra",
]


# Django REST framework
AUTHENTICATION_METHODS = [
    "karrio.server.core.authentication.TokenBasicAuthentication",
    "karrio.server.core.authentication.TokenAuthentication",
    "karrio.server.core.authentication.JWTAuthentication",
    "rest_framework.authentication.SessionAuthentication",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
        "karrio.server.core.permissions.APIAccessPermissions",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": AUTHENTICATION_METHODS,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {"anon": "40/minute", "user": "60/minute"},
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "EXCEPTION_HANDLER": "karrio.server.core.exceptions.custom_exception_handler",
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

# JWT config
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=15),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


# OpenAPI config

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "LOGIN_URL": reverse_lazy("admin:login"),
    "LOGOUT_URL": "/admin/logout",
    "DEFAULT_INFO": "karrio.server.core.views.schema.swagger_info",
    "DEFAULT_AUTO_SCHEMA_CLASS": "karrio.server.core.views.schema.SwaggerAutoSchema",
    "SECURITY_DEFINITIONS": {
        "Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": """
                API keys are used to authenticate requests. You can view and manage your API keys in the Dashboard.

                Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret
                API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

                Authentication to the API is performed via HTTP Basic Auth. Provide your API token as
                the basic auth username value. You do not need to provide a password.

                ```shell
                $ curl https://instance.api.com/v1/shipments \\
                  -u key_c2760bb435l6kj5lk6j5lk671ce3c09b6e:
                # The colon prevents curl from asking for a password.
                ```

                If you need to authenticate via bearer auth (e.g., for a cross-origin request),
                use `-H "Authorization: Token key_c2760bb435l6kj5lk6j5lk671ce3c09b6e"`
                instead of `-u key_c2760bb435l6kj5lk6j5lk671ce3c09b6e`.

                All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure).
                API requests without authentication will also fail.
            """,
        }
    },
}

REDOC_SETTINGS = {
    "LAZY_RENDERING": False,
    "HIDE_HOSTNAME": True,
    "REQUIRED_PROPS_FIRST": True,
    "SPEC_URL": ("schema-json", dict(format=".json")),
}

# Logging configuration

LOG_LEVEL = "DEBUG" if DEBUG else config("LOG_LEVEL", default="INFO")
DJANGO_LOG_LEVEL = "INFO" if DEBUG else config("DJANGO_LOG_LEVEL", default="WARNING")
LOG_FILE_DIR = config("LOG_DIR", default=WORK_DIR)
LOG_FILE_NAME = os.path.join(LOG_FILE_DIR, "debug.log")
DRF_TRACKING_ADMIN_LOG_READONLY = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": LOG_FILE_NAME,
            "when": "D",  # this specifies the interval
            "interval": 1,  # defaults to 1, only necessary for other values
            "backupCount": 20,  # how many backup file to keep, 10 days
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": DJANGO_LOG_LEVEL,
            "propagate": False,
        },
        "karrio": {
            "handlers": ["file", "console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
