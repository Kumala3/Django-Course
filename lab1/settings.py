from utility.config import DbConfig, DjangoConfig
import dj_database_url

DB_URL = DbConfig().db_url()
SECRET_KEY = DjangoConfig().retrieve_secret_key()

# Postgre SQL
DATABASES = {
    "default": dj_database_url.parse(
        url=DB_URL, conn_health_checks=True, conn_max_age=600
    )
}

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "orm",
)

SECRET_KEY = SECRET_KEY
