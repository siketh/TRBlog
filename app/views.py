from flask import render_template
from app import app

# Map this view to this URL
@app.route('/index')
@app.route('/about')
@app.route('/')

# Output this content to the screen for mapped URLs
def index():
	# Temp python dictionary to hold a user name
    user = {'name': 'Trevor'}
    
    # Invokes Jinja2 templating engine, part of Flask framework
    return render_template('index.html', user=user)