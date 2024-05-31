from pathlib import Path

from utility.config import DbConfig, DjangoConfig
import dj_database_url


# Load the configuration
db_conf = DbConfig()
dj_conf = DjangoConfig()

# Get the needed variables for the configuration
DB_URL = db_conf.db_url()
SECRET_KEY = dj_conf.SECRET_KEY
IS_DEBUG = dj_conf.DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/5.0/topics/security/
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run the app with debug turned on in production!
DEBUG = True

# Database configuration
# https://docs.djangoproject.com/en/5.0/ref/databases/
DATABASES = {
    "default": dj_database_url.parse(
        url=DB_URL, conn_health_checks=True, conn_max_age=600
    )
}

# Application configuration
# https://docs.djangoproject.com/en/5.0/ref/applications/
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "orm",
)

# Middleware configuration
# https://docs.djangoproject.com/en/5.0/ref/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Root config to all URLs within an application
ROOT_URLCONF = "urls"

# List of allowed hosts which can use the Django app
ALLOWED_HOSTS = [
    "localhost",
]

# Basic Template configuration
# https://docs.djangoproject.com/en/5.0/howto/overriding-templates/
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
