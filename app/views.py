from flask import render_template
from app import app

# Map this view to this URL
@app.route('/index')
@app.route('/about')
@app.route('/')

# Output this content to the screen for mapped URLs
def about():
    user = {'name': 'Trevor'}
    page = "About"
    
    # Invokes Jinja2 templating engine, part of Flask framework
    return render_template('about.html', user=user, page=page)

@app.route('/blog')
def blog():
    user = {'name': 'Trevor'}
    page = "Blog"
    
    # Invokes Jinja2 templating engine, part of Flask framework
    return render_template('construction.html', user=user, page=page)