from __future__ import print_function
from flask import current_app as app
from . import db, login_manager, bcrypt
from flask import render_template, url_for, flash, redirect, request
from .forms import LoginForm, RegistrationForm, ToDoForm, UpdateAccountForm, MealLogForm, ChallengeForm, EntryForm
from .models import User, Meal, Task, Challenge, Entry
from .mealLog import getTotals
from .dbControl import Control
from flask_login import login_user, logout_user, current_user, login_required, login_manager
import sys

cntr = Control()

@app.route('/home')
def home():
    #db.drop_all()
    #db.create_all()
    return render_template('home.html')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash('Email or Pasword is invalid', 'error')
    return render_template('login.html', title = 'login', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        formData = [form.username.data, form.email.data, form.password.data]
        cntr.addUser(formData)
        flash('Account Created, please sign in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'register', form = form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        cntr.edit(User, form, current_user.id)
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@app.route('/todo/add', methods = ['GET', 'POST'])
@login_required
def new_task():
    form = ToDoForm()
    if form.validate_on_submit():
        flash('Task Added', 'success')
        formData = [form.entry.data]
        cntr.add(Task, formData, current_user)
        return redirect(url_for('toDo'))
    return render_template('toDoAdd.html', title = 'To-Do', form = form)

@app.route('/todo/<int:id>/delete', methods=['POST'])
def delete_tasks(id):
    cntr.delete(Task, id)
    return redirect(url_for('toDo'))

@app.route('/todo', methods = ['GET', 'POST'])
@login_required
def toDo():
    tasks = db.session.query(Task).filter_by(owner=current_user)
    return render_template('toDo.html', title = 'To-Do', tasks = tasks)

@app.route('/meal-log', methods=['GET'])
@login_required
def mealLog():
    meals = db.session.query(Meal).filter_by(owner=current_user)
    return render_template('mealLog.html', title = 'Meal Log', meals = meals, totCal=getTotals("calories", current_user), totFat=getTotals("fat", current_user), totProtein=getTotals("protein", current_user), totCarbs=getTotals("carbs", current_user))

@app.route('/meal-log/add', methods=['GET', 'POST'])
@login_required
def mealLogAdd():
    form = MealLogForm()
    if form.validate_on_submit():
        flash('Meal Added', 'success')
        formData = [form.food.data, form.calories.data, form.servings.data, form.protein.data, form.carb.data, form.fat.data]
        cntr.add(Meal, formData, current_user)
        return redirect(url_for('mealLog'))
    return render_template('mealLogAdd.html', title = 'Meal Log', form = form)

@app.route('/meal-log/<int:id>/delete', methods=['POST'])
def delete_meal(id):
    cntr.delete(Meal, id)
    return redirect(url_for('mealLog'))

@app.route('/meal-log/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_meal(id):
    form = MealLogForm()
    if form.validate_on_submit():
        cntr.edit(Meal, form, id)
        return redirect(url_for('mealLog'))

    return render_template('mealLogEdit.html', title = 'Meal Log', form = form)

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html', title = 'pomodoro timer')

@app.route('/challenges')
def challenges():
    challenges = db.session.query(Challenge)
    return render_template('challenges.html', title = 'Challenges', challenges=challenges)

@app.route('/challenges/create', methods = ['GET', 'POST'])
@login_required
def new_challenges():
    form = ChallengeForm()
    if form.validate_on_submit():
        flash('Challenge Added', 'success')
        formData = [form.title.data, form.description.data]
        cntr.add(Challenge, formData, current_user)
        return redirect(url_for('challenges'))
    return render_template('newChallenges.html', title='Challenges', form=form)

@app.route('/challenges/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_challenge(id):
    form = ChallengeForm()
    edit = db.session.query(Challenge).get_or_404(id)
    if form.validate_on_submit():
        cntr.edit(Challenge, form, id)
        return redirect(url_for('challenges'))

    return render_template('challengeEdit.html', title = 'Challenge', form = form)

@app.route('/challenges/<int:id>/delete', methods=['POST'])
def delete_challenge(id):
    cntr.delete(Challenge, id)
    return redirect(url_for('challenges'))

@app.route('/journal')
@login_required
def journal():
    entries = db.session.query(Entry).filter_by(owner = current_user)
    return render_template('journal.html', entries=entries, title="Journal")

@app.route('/journal/entry', methods=['GET', 'POST'])
@login_required
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        flash('Entry Added', 'success')
        formData = [form.title.data, form.content.data]
        cntr.add(Entry, formData, current_user)
        return redirect(url_for('journal'))
    return render_template('entry.html', title = 'journal', form=form)

@app.route('/journal/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    form = EntryForm()
    edit = db.session.query(Entry).get_or_404(id)
    if form.validate_on_submit():
        cntr.edit(Entry, form, id)
        return redirect(url_for('journal'))

    return render_template('entryEdit.html', title = 'Journal', form = form)

@app.route('/journal/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    cntr.delete(Entry, id)
    return redirect(url_for('journal'))
