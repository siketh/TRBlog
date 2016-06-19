# -*- coding: utf8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# environment
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# prod
#BASE_URL = 'http://trevorroman.com'

# dev
BASE_URL = 'http://localhost:5000'

# pagination
POSTS_PER_PAGE = 5

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
