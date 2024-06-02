from utility.config import DbConfig, DjangoConfig
import dj_database_url


# Load the configuration
db_conf = DbConfig()
dj_conf = DjangoConfig()

SECRET_KEY = dj_conf.SECRET_KEY
db_url = db_conf.db_url()

# Database configuration
# https://docs.djangoproject.com/en/5.0/ref/databases/
DATABASES = {
    "default": dj_database_url.parse(
        url=db_url, conn_max_age=600, conn_health_checks=True
    )
}

# Installed apps definition
# https://docs.djangoproject.com/en/5.0/ref/applications/
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crud",
)

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/5.0/topics/security/
SECRET_KEY = SECRET_KEY
