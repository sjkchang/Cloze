from cloze import db
from cloze.models import User

user = User.query.first()
print(user)
