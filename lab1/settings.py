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
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run the app with debug turned on in production!
DEBUG = False

# Database configuration
DATABASES = {
    "default": dj_database_url.parse(
        url=DB_URL, conn_health_checks=True, conn_max_age=600
    )
}

# Application definition configuration
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "orm",
)
