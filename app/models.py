from datetime import datetime

from flask_security import UserMixin, RoleMixin

from app import db
from sqlalchemy.orm import relationship

post_tag_table = db.Table('post_tag_table',
                          db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                          db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))

post_user_table = db.Table('post_user_table',
                           db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                           db.Column('user_id', db.Integer, db.ForeignKey('user.id')))

user_roles_table = db.Table('user_role_table',
                            db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                            db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


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

    tags = relationship("Tag", secondary=post_tag_table, back_populates="posts")

    def __init__(self, title="", abstract="", body="", repo_url="", user_id=None,  tags=[]):
        self.title = title
        self.abstract = abstract
        self.body = body
        self.created = datetime.now()
        self.updated = self.created
        self.repo_url = repo_url
        self.user_id = user_id
        self.tags = tags

    def __repr__(self):
        return "Post Title: < %s >" % self.title


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255))

    roles = db.relationship('Role', secondary=user_roles_table, backref=db.backref('users', lazy='dynamic'))

    posts = relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, first_name="", last_name="",
                 email="", active=False, confirmed_at=None,
                 password="", roles=[], posts=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active
        self.confirmed_at = confirmed_at
        self.password = password
        self.roles = roles
        self.posts = posts

    def __repr__(self):
        return "User: < %s %s >" % (self.first_name, self.last_name)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return "Role: < %s >" % self.name


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
        return "Tag: < %s >" % self.name
