from flask import render_template, flash, redirect, url_for
from app import app, db, models
from datetime import datetime
from .forms import CreatePostForm

# Map this view to this URL
@app.route('/index')
@app.route('/about')
@app.route('/')
def about():
	post = models.Post.query.filter_by(title='About Me')
	year = date.today().year

	return render_template('post.html', posts=post, year=year)

@app.route('/contact')
def contact():
	post = models.Post.query.filter_by(title='Contact')
	year = date.today().year

	return render_template('post.html', posts=post, year=year)

@app.route('/blog')
def blog():
	posts = models.Post.query.filter(models.Post.title != 'Under Construction').filter(models.Post.title != 'About Me')
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)

@app.route('/create', methods=['GET', 'POST'])
def admin():
	form = CreatePostForm()
	user = models.User.query.filter_by(full_name='Trevor Roman')

	if form.validate_on_submit():
		post = form.title.data, form.abstract.data, form.body.data, form.repo_url.data, str(datetime.now())
		#post_db = models.Post(title=form.title.data, abstract=form.abstract.data, body=form.body.data, repo_url=form.repo_url.data, timestamp=datetime.datetime)
		flash("New Post Created: ")
		flash(post)

	return render_template('admin.html', form=form)
