#!flask/bin/python

# This script is a modification of a script authored by Miguel Grinberg as part of his Flask Mega Tutorial:
# http://blog.miguelgrinberg.com/index

import imp

import config
from app import db, configuration
from migrate.versioning import api

current_config = configuration

v = api.db_version(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
migration = current_config.SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v + 1))
tmp_module = imp.new_module('old_model')
old_model = api.create_model(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(current_config.SQLALCHEMY_DATABASE_URI,
                                          current_config.SQLALCHEMY_MIGRATE_REPO, tmp_module.meta,
                                          db.metadata)
open(migration, "wt").write(script)
api.upgrade(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(current_config.SQLALCHEMY_DATABASE_URI, current_config.SQLALCHEMY_MIGRATE_REPO)
print('New migration saved as ' + migration)
print('Current database version: ' + str(v))
