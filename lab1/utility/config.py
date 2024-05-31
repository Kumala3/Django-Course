from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.yaml", ".secrets.yaml"],
    default_env="default",
    environments=True,
    env="development"
)


class DbConfig:
    """
    Represents the configuration for the database connection.

    Attributes:
        user (str): The username for the database connection.
        password (str): The password for the database connection.
        host (str): The host address for the database connection.
        port (int): The port number for the database connection.
        db (str): The name of the database.

    Methods:
        db_url(): Constructs the database URL based on the provided configuration.

    """

    def __init__(self):
        self.user = settings.get("POSTGRES_USER", "postgres")
        self.password = settings.get("POSTGRES_PASSWORD", None)
        self.host = settings.get("POSTGRES_HOST", "db")
        self.port = settings.get("POSTGRES_PORT", 5432)
        self.db = settings.get("POSTGRES_DB", None)

    def db_url(self) -> str:
        """
        Construct the database URL based on the provided configuration.

        If a password is provided, the database URL will include the password in the format:
        postgres://{user}:{password}@{host}:{port}/{db}

        If no password is provided, the database URL will be in the format:
        postgres://{user}@{host}:{port}/{db}

        Returns:
            str: The database URL.
        """
        if self.password:
            return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        else:
            return f"postgres://{self.user}@{self.host}:{self.port}/{self.db}"


class DjangoConfig:
    """
    DjangoConfig configuration class.

    This class holds settings for Django Configuration.

    Attributes
    ----------
    SECRET_KEY : str
        A string representing the secret key for Django App.
    """

    def __init__(self):
        self.SECRET_KEY = settings.get("SECRET_KEY", None)
        self.DEBUG = settings.get("DEBUG", False)


# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
