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

# Create empty admin interface
admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')


class PostView(ModelView):
    column_exclude_list = ['body', 'abstract']
    column_editable_list = ['title', 'updated', 'repo_url']


admin.add_view(PostView(models.Post, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Tag, db.session))
