from cloze import create_app
from . import db, bcrypt
from .models import User, Meal, Challenge, Entry, Task
from .forms import LoginForm, RegistrationForm, ToDoForm, UpdateAccountForm, MealLogForm, ChallengeForm, EntryForm
from .dbControl import Control
from flask_login import current_user
import pytest

@pytest.fixture(scope='module')
def addTUser():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()

def test_addUser(addTUser):
    control = Control()
    data = ["TestUser", "TestEmail@test.com", "TestPassword"]
    passwordHash = bcrypt.generate_password_hash(data[2]).decode('utf-8')
    control.addUser(data)
    user = User.query.filter_by(email=data[1]).first()
    assert(user.username == 'TestUser')
    assert(user.email == "TestEmail@test.com")
    assert(user.password_hash != "TestPassword")

@pytest.fixture(scope='module')
def delete():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()

def test_delete(delete):
    control = Control()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal = Meal(food="Test Food", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    challenge = Challenge(title="Test Challenge", description="Test description", owner=user)
    task = Task(entry = "Test Task", owner=user)
    entry = Entry(title="Test Entry", content="Test content", owner=user)
    db.session.add(user)
    db.session.add(meal)
    db.session.add(challenge)
    db.session.add(task)
    db.session.add(entry)
    db.session.commit()
    assert(User.query.all() != None)
    assert(Meal.query.all() != None)
    assert(Challenge.query.all() != None)
    assert(Task.query.all() != None)
    assert(Entry.query.all() != None)
    control.delete(Meal, meal.id)
    control.delete(Challenge, challenge.id)
    control.delete(Task, task.id)
    control.delete(Entry, entry.id)
    control.delete(User, user.id)
    assert(User.query.all() == [])
    assert(Meal.query.all() == [])
    assert(Challenge.query.all() == [])
    assert(Task.query.all() == [])
    assert(Entry.query.all() == [])

@pytest.fixture(scope='module')
def addTest():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    db.session.add(user)
    db.session.commit()


def test_add(addTest):
    control = Control()
    user = User.query.filter_by(id=1).first()

    assert(len(Meal.query.all()) == 0)
    mealData = ["Test Food", 100, 2, 5, 4, 3]
    control.add(Meal, mealData, user)
    meal = Meal.query.filter_by(id=1).first()
    assert(len(Meal.query.all()) == 1)
    assert(meal.food == "Test Food")
    assert(meal.calories == 100)
    assert(meal.servings == 2)
    assert(meal.protein == 5)
    assert(meal.carbs == 4)
    assert(meal.fats == 3)

    assert(len(Task.query.all()) == 0)
    taskData = ["Test Entry"]
    control.add(Task, taskData, user)
    task = Task.query.filter_by(id=1).first()
    assert(len(Task.query.all()) == 1)
    assert(task.entry == "Test Entry")

    assert(len(Entry.query.all()) == 0)
    entryData= ["Test Title", "Test Content"]
    control.add(Entry, entryData, user)
    entry = Entry.query.filter_by(id=1).first()
    assert(len(Entry.query.all()) == 1)
    assert(entry.title == "Test Title")
    assert(entry.content == "Test Content")

    assert(len(Challenge.query.all()) == 0)
    challengeData = ["Test Challenge", "Test description"]
    control.add(Challenge, challengeData, user)
    challenge = Challenge.query.filter_by(id=1).first()
    assert(len(Challenge.query.all()) == 1)
    assert(challenge.title == "Test Challenge")
    assert(challenge.description == "Test description")
