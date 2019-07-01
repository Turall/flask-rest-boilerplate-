from core.settings.base import Config


class TestingConfig(Config):
    """ Configuration class for site development environment """

    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgres:///gotham_test"
