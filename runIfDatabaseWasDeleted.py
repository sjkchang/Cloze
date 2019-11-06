from cloze import db
from cloze.models import User, Meal

db.drop_all()
db.create_all()
