from flask import render_template
from app import app, db, models
from datetime import date

# Map this view to this URL
@app.route('/index')
@app.route('/about')
@app.route('/')

# Output this content to the screen for mapped URLs
def about():
	post = models.Post.query.filter_by(title='About Me').first()
	title = post.title
	abstract = post.abstract
	body = post.body
	author = post.author
	year = date.today().year

	# Invokes Jinja2 templating engine, part of Flask framework
	return render_template('post.html', title=title, abstract=abstract, body=body, author=author, year=year)

@app.route('/blog')
def blog():
	post = models.Post.query.filter_by(title='Under Construction').first()
	title = post.title
	abstract = post.abstract
	body = post.body
	author = post.author
	year = date.today().year

	# Invokes Jinja2 templating engine, part of Flask framework
	return render_template('post.html', title=title, abstract=abstract, body=body, author=author, year=year)

@app.route('/example')
def example():
	post = models.Post.query.filter_by(title='About Me').first()
	title = post.title
	abstract = post.abstract
	body = post.body
	author = post.author
	year = date.today().year

	# Invokes Jinja2 templating engine, part of Flask framework
	return render_template('eaxmple_post.html', title=title, abstract=abstract, body=body, author=author, year=year)