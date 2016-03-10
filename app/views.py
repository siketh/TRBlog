from flask import render_template, flash, redirect, url_for
from app import app, db, models
from datetime import datetime, date
from .forms import PostForm, SelectForm

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

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	admin = models.User.query.filter_by(full_name='Trevor Roman').first()
	
	select_form = SelectForm()
	post_form = PostForm()

	select_form.reset()

	# Button debugging
	flash("Edit: " + str(select_form.edit.data))
	flash("Delete: " + str(select_form.delete.data))
	flash("New: " + str(select_form.new.data))
	flash("Save: " + str(post_form.save.data))
	flash("Cancel: " + str(post_form.cancel.data))

	# If the Edit button is clicked
	if select_form.edit.data:
		selected_post = models.Post.query.filter_by(id=select_form.posts.data).first()

		post_form.title.data = selected_post.title
		post_form.abstract.data = selected_post.abstract
		post_form.body.data = selected_post.body
		post_form.repo_url.data = selected_post.repo_url

		flash("Post Selected: ")
		flash(selected_post.title)

		select_form.edit.data = False

	# If the Delete button is clicked
	elif select_form.delete.data:
		selected_post = models.Post.query.filter_by(id=select_form.posts.data).first()
		deleted_post = post_form.title.data

		post_form.title.data = selected_post.title
		post_form.abstract.data = selected_post.abstract
		post_form.body.data = selected_post.body
		post_form.repo_url.data = selected_post.repo_url

		db.session.delete(selected_post)
		db.session.commit()

		post_form.clear()
		select_form.reset()

		flash("Post Deleted: ")
		flash(deleted_post)

		select_form.delete.data = False
	
	# If the New button is clicked
	elif select_form.new.data:
		post_form.clear()
		select_form.reset()

		flash("Post Created: ")

		select_form.new.data = False

	# If the Save button is clicked 
	elif post_form.save.data:
		# If the post is valid
		if post_form.validate_on_submit():
			title = post_form.title.data
			abstract = post_form.abstract.data
			body = post_form.body.data
			repo_url = post_form.repo_url.data

			# TODO: Posts cannot be updated, implement a solution, possibly by looking up title/id
			# If the current post already exists, update it
			selected_post = None
			if selected_post is not None:
				selected_post.title = title
				selected_post.abstract = abstract
				selected_post.body = body
				selected_post.repo_url = repo_url
				selected_post.updated = datetime.today()
				
				db.session.commit()

			# Otherwise it doesn't exist, so create a new entry
			else:
				created = datetime.today()
				selected_post = models.Post(author=admin, title=title, abstract=abstract, body=body, repo_url=repo_url, created=created)
				
				db.session.add(selected_post)
				db.session.commit()

			select_form.reset()

			flash("Post Saved: ")
			flash(post_form.title.data)
			flash(datetime.today())

			post_form.save.data = False
		
		# If the post is not valid
		else:
			flash("Post Cannot be Saved: ")
			flash("One or more validators did not pass")

			post_form.save.data = False

	# If the cancel button is clicked
	elif post_form.cancel.data:
		post_form.clear()
		select_form.reset()

		flash("Post Canceled: ")
		flash(post_form.title.data)

		post_form.cancel.data = False
	
	return render_template('admin.html', select_form=select_form, post_form=post_form)