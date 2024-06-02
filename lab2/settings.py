from utility.config import DbConfig, DjangoConfig
import dj_database_url


# Load the configuration
db_conf = DbConfig()
dj_conf = DjangoConfig()

SECRET_KEY = dj_conf.SECRET_KEY
db_url = db_conf.db_url()

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/5.0/topics/security/
SECRET_KEY = SECRET_KEY

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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
