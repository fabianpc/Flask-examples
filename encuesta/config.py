import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '4574e033d677b3bcc508d88f'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://asayiiizmnigtd:ddd64f69c6d677d60d5441d5960f065a59687203848bc9fa4c7712ac2b57149d@ec2-54-159-107-189.compute-1.amazonaws.com:5432/dbm7dmjkhmkrgp'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://tester:secreto@localhost:5432/encuesta'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://producer:secreto@localhost:5432/encuesta'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
