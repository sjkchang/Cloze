from cloze import create_app
from . import db, bcrypt
from .models import User, Meal
from .mealLog import getTotals, getTotalCalories, getTotalFat, getTotalCarbs, getTotalProtein
import pytest

@pytest.fixture(scope='module')
def getTotal():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal1 = Meal(food="Test Food One", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    meal2 = Meal(food="Test Food Two", servings=2, calories=33, protein=2, carbs=4, fats=6, owner=user)
    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

def test_getTotals(getTotal):
    user = User.query.filter_by(email="TestEmail@test.com").first()
    assert(getTotals("calories", user) == 166)
    assert(getTotals("fat", user) == 17)
    assert(getTotals("carbs", user) == 11)
    assert(getTotals("protein", user) == 5)

@pytest.fixture(scope='module')
def getTotalCals():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal1 = Meal(food="Test Food One", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    meal2 = Meal(food="Test Food Two", servings=2, calories=33, protein=2, carbs=4, fats=6, owner=user)
    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

def test_getTotalCalories(getTotalCals):
    user = User.query.filter_by(email="TestEmail@test.com").first()
    assert(getTotalCalories(user) == 166)

@pytest.fixture(scope='module')
def getTotalFats():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal1 = Meal(food="Test Food One", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    meal2 = Meal(food="Test Food Two", servings=2, calories=33, protein=2, carbs=4, fats=6, owner=user)
    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

def test_getTotalFat(getTotalFats):
    user = User.query.filter_by(email="TestEmail@test.com").first()
    assert(getTotalFat(user) == 17)

@pytest.fixture(scope='module')
def getTotalCarb():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal1 = Meal(food="Test Food One", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    meal2 = Meal(food="Test Food Two", servings=2, calories=33, protein=2, carbs=4, fats=6, owner=user)
    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

def test_getTotalCarbs(getTotalCarb):
    user = User.query.filter_by(email="TestEmail@test.com").first()
    assert(getTotalCarbs(user) == 11)

@pytest.fixture(scope='module')
def getTotalProteins():
    app = create_app(True)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    passwordHash = bcrypt.generate_password_hash("TestPassword").decode('utf-8')
    user = User(username="TestUser", email="TestEmail@test.com", password_hash=passwordHash)
    meal1 = Meal(food="Test Food One", servings=1, calories=100, protein=1, carbs=3, fats=5, owner=user)
    meal2 = Meal(food="Test Food Two", servings=2, calories=33, protein=2, carbs=4, fats=6, owner=user)
    db.session.add(meal1)
    db.session.add(meal2)
    db.session.commit()

def test_getTotalProtein(getTotalProteins):
    user = User.query.filter_by(email="TestEmail@test.com").first()
    assert(getTotalProtein(user) == 5)
