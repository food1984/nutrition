import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'test_app.db'))
    TESTING = True
    FIXTURES_DIRS = ['../tests/integrations/fixtures']


class ProductionConfig(Config):
    pass
