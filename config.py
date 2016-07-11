# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

environment = os.environ.get('ENV')

if environment is None:
    # environment
    CSRF_ENABLED = True
    SECRET_KEY = 'temp-secret-key'
    DEV_MODE = True
    DEBUG_MODE = True
    LOGGING_ENABLED = True
    TESTING = False

    # for RSS
    BASE_URL = 'http://localhost:5000'

    # pagination
    POSTS_PER_PAGE = 5

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

elif environment == 'DEV':
    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')

elif environment == 'TEST':
    # environment
    DEV_MODE = False
    DEBUG_MODE = False
    TESTING = True

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

elif environment == 'PROD':
    # environment
    DEV_MODE = False
    DEBUG_MODE = False

    # for RSS
    BASE_URL = 'http://www.trevorroman.com'

    # pagination
    POSTS_PER_PAGE = 20

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
