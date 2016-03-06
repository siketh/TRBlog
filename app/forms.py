from flask.ext.wtf import Form
from wtforms import TextAreaField, validators

class CreatePostForm(Form):
	title = TextAreaField('Title', [validators.Length(min=1, max=100)])
	abstract = TextAreaField('Title', [validators.Length(min=1, max=1000)])
	body = TextAreaField('Title', [validators.Length(min=1, max=10000)])
	repo_url = TextAreaField('Title', [validators.Length(max=200)])

