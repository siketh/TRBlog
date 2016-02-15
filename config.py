import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Required by Flask-SQLAlchemy, path to db file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Stores SQLAlchemy migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Activates cross-site forgery prevention
WTF_CSRF_ENABLED = True

# Needed when CSRF is enabled
SECRET_KEY = 'you-will-never-guess'