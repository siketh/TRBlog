from app import db

# Users are created as instances of the db.Model class
class User(db.Model):
	# Fields are created as instances of the db.Column class
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # Not actually a database field, a relationship. This is the one side of 
    # the one-to-many relationship. The first parameter is the many side of 
    # the one-to-many relationship. This will get teh list of posts relating
    # to the user. Backref defines the field from the many class, that points
    # to the one object.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Verify a user is allowed to authenticate
    @property
    def is_authenticated(self):
        return True

    # Verify a user is not banned
    @property
    def is_active(self):
        return True

    # Verify a user is not anonymous (fake)
    @property
    def is_anonymous(self):
        return False

    # Return a unique identifier for the user
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    # Tells python to print objects of this class (for debugging)
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    # A foreign key, SQLAlchemy will know that this field will link to a User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)