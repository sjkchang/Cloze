from cloze import app, db, bcrypt
from models import User
from flask_login import current_user
import pytest

@pytest.fixture(scope='module')
def new_user():
    passwordHash = bcrypt.generate_password_hash('testPassword').decode('utf-8')
    user = User(username="testuser", email="testEmail@gmail.com", password_hash=passwordHash)
    return user

def test_new_user(new_user):
    assert new_user.username == "testuser"
    assert new_user.email == 'testEmail@gmail.com'
    assert new_user.password_hash != 'testPassword'
    assert new_user.is_authenticated
