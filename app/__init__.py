from config import DEV_MODE, DEBUG_MODE
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

# Initialize flask application
app = Flask(__name__)

# Initialize configuration
app.config.from_object('config')

# Initialize database
db = SQLAlchemy(app)

# Initialize markdown
Markdown(app)

from app.views import main, errors, rss
from app import models


class PostView(ModelView):
    column_exclude_list = ['body', 'abstract']
    column_editable_list = ['title', 'updated', 'repo_url']


if DEV_MODE:
    # Create empty admin interface
    admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')
    admin.add_view(PostView(models.Post, db.session))
    admin.add_view(ModelView(models.User, db.session))
    admin.add_view(ModelView(models.Tag, db.session))

if not DEBUG_MODE:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('log/TRBlog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('TRBlog Log')