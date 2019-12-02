from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(userId):
    return User.query.get(int(userId))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    list = db.relationship('Task', backref='owner', lazy=True)
    meal = db.relationship('Meal', backref='owner', lazy=True)
    challenge = db.relationship('Challenge', backref='owner', lazy=True)
    entry = db.relationship('Entry', backref='owner', lazy=True)

    def __repr__(self):
        return '<user: {}, email: {}>'.format(self.username, self.email)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(128), index=True, nullable=False)
    servings = db.Column(db.Integer, index=True)
    calories = db.Column(db.Integer, index=True)
    protein = db.Column(db.Integer, index=True)
    carbs = db.Column(db.Integer, index=True)
    fats = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(256), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.String(512), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    description = db.Column(db.String(512), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
