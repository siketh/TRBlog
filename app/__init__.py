# This scrip creates an application object of class Flask,
# then imports the views module

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir

# Initialize flask application
app = Flask(__name__)

# Initialize configuration
app.config.from_object('config')

# Initialize database
db = SQLAlchemy(app)

from app import views, models