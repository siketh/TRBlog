from datetime import datetime

from app import db
from sqlalchemy.orm import relationship

post_tag_table = db.Table('post_tag_table',
                          db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                          db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                          )

post_user_table = db.Table('post_user_table',
                           db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                           db.Column('user_id', db.Integer, db.ForeignKey('user.id')))


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    abstract = db.Column(db.String(1000))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    repo_url = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    tags = relationship(
        "Tag",
        secondary=post_tag_table,
        back_populates="posts")

    def __init__(self, title="", abstract="", body="", repo_url="", tags=[]):
        self.title = title
        self.abstract = abstract
        self.body = body
        self.created = datetime.now()
        self.updated = self.created
        self.repo_url = repo_url
        self.user_id = None
        self.tags = tags

    def __repr__(self):
        return self.title


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    full_name = db.Column(db.String(64), index=True, unique=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    posts = relationship(
        'Post',
        backref='author',
        lazy='dynamic')

    def __init__(self, first_name="", last_name="", full_name="", nickname="", email="", posts=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.nickname = nickname
        self.email = email
        self.posts = posts

    def __repr__(self):
        return self.full_name


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    posts = relationship(
        "Post",
        secondary=post_tag_table,
        back_populates="tags")

    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return self.name
