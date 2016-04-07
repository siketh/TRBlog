from flask import render_template, redirect, url_for
from app import app, models
from datetime import date
from config import POSTS_PER_PAGE

@app.route('/')
@app.route('/index')
def index():
	return redirect(url_for('blog'))

@app.route('/blog')
@app.route('/blog/<int:page_index>')
def blog(page_index=1):
	posts = models.Post.query \
		.filter(~models.Post.tags.any(models.Tag.name.in_(['About', 'Contact']))) \
		.order_by(models.Post.updated) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	year = date.today().year

	return render_template('post.html', page='blog', posts=posts, year=year)

@app.route('/about')
@app.route('/about/<int:page_index>')
def about(page_index=1):
	posts = models.Post.query \
		.filter(models.Post.tags.any(models.Tag.name.in_(['About']))) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	year = date.today().year

	return render_template('post.html', page='about', posts=posts, year=year)

@app.route('/contact')
@app.route('/contact/<int:page_index>')
def contact(page_index=1):
	posts = models.Post.query \
		.filter(models.Post.tags.any(models.Tag.name.in_(['Contact']))) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	year = date.today().year

	return render_template('post.html', page='contact', posts=posts, year=year)

@app.errorhandler(404)
def page_not_found(e):
	year = date.today().year

	return render_template('404.html', posts=[], year=year), 404
	