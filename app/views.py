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
@app.route('/blog/post/<int:post_id>')
def blog(page_index=1, post_id=None):
	year = date.today().year

	if post_id is not None:
		posts = models.Post.query.filter_by(id=post_id) \
			.paginate(page_index, POSTS_PER_PAGE, False)
	else:
		posts = models.Post.query \
			.filter(~models.Post.tags.any(models.Tag.name.in_(['about', 'contact']))) \
			.order_by(models.Post.updated.desc()) \
			.paginate(page_index, POSTS_PER_PAGE, False)

	return render_template('post.html', page='blog', posts=posts, year=year)

@app.route('/about')
@app.route('/about/<int:page_index>')
def about(page_index=1):
	posts = models.Post.query \
		.filter(models.Post.tags.any(models.Tag.name.in_(['about']))) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	year = date.today().year

	return render_template('post.html', page='about', posts=posts, year=year)

@app.route('/contact')
@app.route('/contact/<int:page_index>')
def contact(page_index=1):
	posts = models.Post.query \
		.filter(models.Post.tags.any(models.Tag.name.in_(['contact']))) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	year = date.today().year

	return render_template('post.html', page='contact', posts=posts, year=year)

@app.route('/tags')
@app.route('/tags/<tag_name>')
@app.route('/tags/<tag_name>/<int:page_index>')
@app.route('/tags/<tag_name>/post/<int:post_id>')
def tags(page_index=1, tag_name=None, post_id=None):
	year = date.today().year

	if post_id is not None:
		posts = models.Post.query.filter_by(id=post_id) \
			.paginate(page_index, POSTS_PER_PAGE, False)
	
	else: 
		posts = models.Post.query \
		.filter(models.Post.tags.any(models.Tag.name.in_([tag_name]))) \
		.paginate(page_index, POSTS_PER_PAGE, False)

	return render_template('post.html', page='blog', posts=posts, year=year)

@app.errorhandler(404)
def page_not_found(e):
	year = date.today().year

	return render_template('404.html', posts=[], year=year), 404
	