
from cloze import app, db, bcrypt, login_manager
from cloze.models import User

passwordHash = bcrypt.generate_password_hash('ayoooo').decode('utf-8')
user = User(username='sup', email='hey@gmail.com', password_hash=passwordHash)
print(user.username.data, user.email.data, passwordHash)
