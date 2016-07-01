# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# environment
CSRF_ENABLED = True
SECRET_KEY = 'temp-secret-key'
DEV_MODE = True
DEBUG_MODE = False
# prod
#BASE_URL = 'http://trevorroman.com'

# dev
BASE_URL = 'http://localhost:5000'

# pagination
POSTS_PER_PAGE = 5

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
