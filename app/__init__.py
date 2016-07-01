from config import DEV_MODE, LOGGING_ENABLED
from flask import Flask
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

if DEV_MODE:
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView


    class PostView(ModelView):
        column_exclude_list = ['body', 'abstract']
        column_editable_list = ['title', 'updated', 'repo_url']


    # Create empty admin interface
    admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')
    admin.add_view(PostView(models.Post, db.session))
    admin.add_view(ModelView(models.User, db.session))
    admin.add_view(ModelView(models.Tag, db.session))

if LOGGING_ENABLED:
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('log/TRBlog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

