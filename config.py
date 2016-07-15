# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# get configuration to use from a system environment variable
environment = os.environ.get('ENV')

#######################################
# default configuration (development) #
#######################################

# environmental
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

#######################################
# environment specific configurations #
#######################################

if environment == 'TEST':
    DEV_MODE = False
    DEBUG_MODE = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

elif environment == 'PROD':
    DEV_MODE = False
    DEBUG_MODE = False
    BASE_URL = 'http://www.trevorroman.com'
    POSTS_PER_PAGE = 20
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod.db')
