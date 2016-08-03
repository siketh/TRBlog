import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

# Initialize flask application
app = Flask(__name__)

# Initialize configuration
app.config.from_object('config')

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize markdown
Markdown(app)

# Initialize further dependencies
from app.views import main, errors, rss
from app import models

# Initialize flask-security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
# user_datastore.find_or_create_role(name='admin', description='Administrator')
security = Security(app, user_datastore)

# Initialize logger
file_handler = RotatingFileHandler('log/TRBlog.log', 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# Override default admin views
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

# Initialize custom admin views
admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')
admin.add_view(PostView(models.Post, db.session))
admin.add_view(UserView(models.User, db.session))
admin.add_view(TagView(models.Tag, db.session))
