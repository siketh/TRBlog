from flask import render_template
from app import app, db, models
from datetime import date

# Map this view to this URL
@app.route('/index')
@app.route('/about')
@app.route('/')
def about():
	posts = models.Post.query.filter_by(title='About Me')
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/contact')
def contact():
	posts = models.Post.query.filter_by(title='Contact')
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/blog')
def blog():
	posts = models.Post.query.filter(models.Post.title != 'Under Construction').filter(models.Post.title != 'About Me')
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/example')
def example():
	post = models.Post.query.filter_by(title='About Me').first()
	year = date.today().year

	return render_template('eaxmple_post.html', posts=posts, year=year)