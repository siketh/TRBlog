#!flask/bin/python

# This code is authored by Miguel Grinberg as part of his Flask Mega Tutorial:
# http://blog.miguelgrinberg.com/index

from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from migrate.versioning import api

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
