from cloze import db, bcrypt
from flask import flash
from .models import User, Meal, Task, Challenge, Entry
from flask_login import current_user

class Control():
    def delete(self, type, id):
        delete = db.session.query(type).get_or_404(id)
        db.session.delete(delete)
        db.session.commit()

    def edit(self, type, form, id):
        edit = db.session.query(type).get_or_404(id)
        if(type == Meal):
            edit.food = form.food.data
            edit.servings = form.servings.data
            edit.calories = form.calories.data
            edit.protein = form.protein.data
            edit.carbs = form.carb.data
            edit.fats = form.fat.data
        if(type == Challenge):
            edit.title = form.title.data
            edit.description = form.description.data
        if(type == Entry):
            edit.title = form.title.data
            edit.content = form.content.data
        if(type == User):
            edit.username = form.username.data
            edit.email = form.email.data

        db.session.commit()

    def add(self, type, formData, user):
        if(type == Challenge):
            challenge = Challenge(title=formData[0], description=formData[1], owner=user)
            db.session.add(challenge)
            db.session.commit()

        if(type == Task):
            task = Task(entry=formData[0], owner=user)
            db.session.add(task)
            db.session.commit()

        if(type == Meal):
            meal = Meal(food=formData[0], calories=formData[1], servings=formData[2], protein=formData[3], carbs=formData[4], fats=formData[5], owner=user)
            db.session.add(meal)
            db.session.commit()

        if(type == Entry):
            entry = Entry(title=formData[0], content=formData[1], owner=user)
            db.session.add(entry)
            db.session.commit()

    def addUser(self, formData):
        passwordHash = bcrypt.generate_password_hash(formData[2]).decode('utf-8')
        testUser = User(username=formData[0], email=formData[1], password_hash=passwordHash)
        db.session.add(testUser)
        db.session.commit()
