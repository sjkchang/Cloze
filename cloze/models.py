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
    #planner = db.relationship('DailyPlanner', backref='owner', lazy=True)
    meal = db.relationship('Meal', backref='owner', lazy=True)

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


class DailyPlanner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    six = db.Column(db.String(256), index=True)
    six30 = db.Column(db.String(256), index=True)
    seven = db.Column(db.String(256), index=True)
    seven30 = db.Column(db.String(256), index=True)
    eight = db.Column(db.String(256), index=True)
    eight30 = db.Column(db.String(256), index=True)
    nine = db.Column(db.String(256), index=True)
    nine30 = db.Column(db.String(256), index=True)
    ten = db.Column(db.String(256), index=True)
    ten30 = db.Column(db.String(256), index=True)
    eleven = db.Column(db.String(256), index=True)
    eleven30 = db.Column(db.String(256), index=True)
    twelve = db.Column(db.String(256), index=True)
    twelve30 = db.Column(db.String(256), index=True)
    thirteen = db.Column(db.String(256), index=True)
    thirteen30 = db.Column(db.String(256), index=True)
    fourteen = db.Column(db.String(256), index=True)
    fourteen30 = db.Column(db.String(256), index=True)
    fifteen = db.Column(db.String(256), index=True)
    fifteen30 = db.Column(db.String(256), index=True)
    sixteen = db.Column(db.String(256), index=True)
    sixteen30 = db.Column(db.String(256), index=True)
    seventeen = db.Column(db.String(256), index=True)
    seventeen30 = db.Column(db.String(256), index=True)
    eighteen = db.Column(db.String(256), index=True)
    eighteen30 = db.Column(db.String(256), index=True)
    nineteen = db.Column(db.String(256), index=True)
    nineteen30 = db.Column(db.String(256), index=True)
    twenty = db.Column(db.String(256), index=True)
    twenty30 = db.Column(db.String(256), index=True)
    twentyone = db.Column(db.String(256), index=True)
    twentyone30 = db.Column(db.String(256), index=True)
    twentytwo = db.Column(db.String(256), index=True)
    twentytwo30 = db.Column(db.String(256), index=True)
    twentythree = db.Column(db.String(256), index=True)
    twentythree30 = db.Column(db.String(256), index=True)
