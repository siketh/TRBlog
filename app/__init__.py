# This scrip creates an application object of class Flask,
# then imports the views module

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir, SQLALCHEMY_DATABASE_URI
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flaskext.markdown import Markdown

# Initialize flask application
app = Flask(__name__)

# Initialize configuration
app.config.from_object('config')

# Initialize database
db = SQLAlchemy(app)

# Create empty admin interface
admin = Admin(app, name='trevorroman.com', template_mode='bootstrap3')

Markdown(app)

from app import views, models

admin.add_view(ModelView(models.Post, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Tag, db.session))