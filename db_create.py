#!flask/bin/python

# This script is a modification of a script authored by Miguel Grinberg as part of his Flask Mega Tutorial:
# http://blog.miguelgrinberg.com/index

import os.path

from app import db, configuration
from migrate.versioning import api

current_config = configuration

db.create_all()

if not os.path.exists(current_config.SQLALCHEMY_MIGRATE_REPO):
    api.create(current_config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO, api.version(
        current_config.SQLALCHEMY_MIGRATE_REPO))
