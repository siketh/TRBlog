from flask import render_template, flash, redirect, url_for
from app import app, db, models, Session
from datetime import datetime, date
from .forms import PostForm, SelectForm

# Map this view to this URL
@app.route('/blog')
def blog():
	session = Session()
	posts = session.query(models.User).order_by(models.User.id)
	year = date.today().year

	return render_template('post.html', posts=posts, year=year)
