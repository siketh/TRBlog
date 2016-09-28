# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = None
SECRET_KEY = None
DEV_MODE = None
DEBUG_MODE = None
TESTING = None
BASE_URL = None
POSTS_PER_PAGE = None
SQLALCHEMY_DATABASE_URI = None
SQLALCHEMY_MIGRATE_REPO = None
SQLALCHEMY_TRACK_MODIFICATIONS = None


class Config(object):
    # environmental
    CSRF_ENABLED = True
    #SECRET_KEY = <SET AFTER DEPLOYMENT>
    DEV_MODE = True
    DEBUG_MODE = True
    TESTING = False

    # for RSS
    BASE_URL = 'http://localhost:5000'

    # pagination
    POSTS_PER_PAGE = 5

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    DEV_MODE = False
    DEBUG_MODE = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


class ProdConfig(Config):
    DEV_MODE = False
    DEBUG_MODE = False
    BASE_URL = 'http://www.trevorroman.com'
    POSTS_PER_PAGE = 20
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.db')


def get_config():
    environment = os.environ['ENV']

    print("Current environment: " + environment)

    if environment == 'PROD':
        print("Creating production configuration")
        current_config = ProdConfig()
    elif environment == 'TEST':
        print("Creating production configuration")
        current_config = TestConfig()
    else:
        print("Creating development configuration")
        current_config = Config()

    return current_config
