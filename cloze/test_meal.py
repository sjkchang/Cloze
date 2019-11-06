from cloze import app, db, bcrypt
from models import User, Meal
import pytest

@pytest.fixture(scope='module')
def new_meal():
    passwordHash = bcrypt.generate_password_hash('testPassword').decode('utf-8')
    user = User(username="testuser", email="testEmail@gmail.com", password_hash=passwordHash)
    meal = Meal(food='testMeal', servings='2', calories='100', protein='5', carbs='2', fats='3', owner=user)
    return meal

def test_new_user(new_meal):
    assert new_meal.food == "testMeal"
    assert new_meal.servings == '2'
    assert new_meal.calories == '100'
    assert new_meal.protein == '5'
    assert new_meal.carbs == '2'
    assert new_meal.fats == '3'
    assert new_meal.owner.username == "testuser"
