from cloze import db
from cloze.models import User

db.drop_all()
db.create_all()
