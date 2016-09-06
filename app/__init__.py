import logging
import os
from logging.handlers import RotatingFileHandler

import config
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_security import current_user, Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)


class PostView(ModelView):
    column_exclude_list = ['body', 'abstract']
    column_editable_list = ['title', 'updated', 'repo_url']

    def is_accessible(self):
        return current_user.has_role('admin')


class UserView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')


class TagView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')


def init_configuration():
    current_config = config.get_config()

    app.config.from_object(current_config)

    return current_config


def init_database_connection():
    return SQLAlchemy(app)


def init_login_manager():
    lm = LoginManager()
    lm.init_app(app)

    return lm


def init_markdown():
    return Markdown(app)


def init_logger():
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    file_handler = RotatingFileHandler('log/TRBlog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

    return app.logger


def init_admin():
    # Initialize flask-security
    user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
    security = Security(app, user_datastore)

    # Initialize custom admin views
    admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')
    admin.add_view(PostView(models.Post, db.session))
    admin.add_view(UserView(models.User, db.session))
    admin.add_view(TagView(models.Tag, db.session))

    return admin


configuration = init_configuration()
db = init_database_connection()
login_manager = init_login_manager()
markdown = init_markdown()
logger = init_logger()

from app.views import main, errors, rss
from app import views, models

admin = init_admin()
