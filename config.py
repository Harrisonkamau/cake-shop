
WTF_CSRF_ENABLED = True


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'hialreuhsan.ndjfbfhgfhfhfre'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:bonus.db"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
