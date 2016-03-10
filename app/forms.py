from flask.ext.wtf import Form
from app import db, models
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, validators

class PostForm(Form):
	title = TextAreaField('Title', [validators.Length(min=1, max=100)])
	abstract = TextAreaField('Title', [validators.Length(min=1, max=1000)])
	body = TextAreaField('Title', [validators.Length(min=1, max=10000)])
	repo_url = TextAreaField('Title', [validators.Length(max=200)])
	save = SubmitField(label='Save')
	cancel = SubmitField(label='Cancel')

	def clear(self):
		self.title.data = None
		self.abstract.data = None
		self.body.data = None
		self.repo_url.data = None


class SelectForm(Form):
	posts = SelectField('Posts', coerce=int)
	edit = SubmitField(label='Edit')
	delete = SubmitField(label='Delete')
	new = SubmitField(label='New')

	def reset(self):
		posts = models.Post.query.all()
		self.posts.choices = [(post.id, post.title) for post in posts]