from cloze import db, bcrypt
from flask import flash
from models import User, Meal, Task, Challenge, Entry
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

    def add(self, type, form):
        if(type == Challenge):
            flash('Challenge Added', 'success')
            challenge = Challenge(title=form.title.data, description=form.description.data, owner=current_user)
            db.session.add(challenge)
            db.session.commit()

        if(type == Task):
            flash('Task Added', 'success')
            entry = Task(entry = form.entry.data, owner=current_user)
            db.session.add(entry)
            db.session.commit()

        if(type == Meal):
            flash('Meal Added', 'success')
            meal = Meal(food=form.food.data, servings=form.servings.data, calories=form.calories.data, protein=form.protein.data, carbs=form.carb.data, fats=form.fat.data, owner=current_user)
            db.session.add(meal)
            db.session.commit()

        if(type == Entry):
            flash('Entry Added', 'success')
            entry = Entry(title=form.title.data, content=form.content.data, owner=current_user)
            db.session.add(entry)
            db.session.commit()

        if(type == User):
            passwordHash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password_hash=passwordHash)
            db.session.add(user)
            db.session.commit()
            flash('Account Created, please sign in', 'success')
