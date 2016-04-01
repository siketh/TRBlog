from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

post_tag_table = Table('post_tag_table', Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

post_user_table = Table('post_user_table', Base.metadata,
    Column('post_id', Integer, ForeignKey('post.id')),
    Column('user_id', Integer, ForeignKey('user.id')))

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    title = db.Column(db.String(100))
    abstract = db.Column(db.String(1000))
    body = db.Column(db.String(10000))
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
        return '<Post Title %r>' % (self.title)

class User(Base):
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
        return '<User Name %r>' % (self.full_name)

class Tag(Base):
    __tablename__ = 'tag'
    
    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    posts = relationship(
        "Post",
        secondary=post_tag_table,
        back_populates="tags")

    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return '<Tag Name %r>' % (self.name)