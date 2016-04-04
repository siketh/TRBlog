from flask import render_template
from app import app, models, Session
from datetime import date

@app.route('/about')
def about():
	session = Session()
	posts = session.query(models.Post).filter(models.Post.tags.any(models.Tag.name.in_(['About'])))
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/contact')
def contact():
	session = Session()
	posts = session.query(models.Post).filter(models.Post.tags.any(models.Tag.name.in_(['Contact'])))
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/blog')
def blog():
	session = Session()
	posts = session.query(models.Post).filter(~models.Post.tags.any(models.Tag.name.in_(['About', 'Contact']))).order_by(models.Post.updated)
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.errorhandler(404)
def page_not_found(e):
	year = date.today().year

	return render_template('404.html', posts=[], year=year), 404
	