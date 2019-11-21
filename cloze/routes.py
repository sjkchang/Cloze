from cloze import app, db, bcrypt, login_manager
from flask import render_template, url_for, flash, redirect, request
from forms import LoginForm, RegistrationForm, ToDoForm, UpdateAccountForm, MealLogForm, ClearDBForm
from models import User, Meal, Task
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/journal')
@login_required
def journal():
    return render_template('journal.html')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_active:
        redirect(url_for('home'))
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
        passwordHash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=passwordHash)
        db.session.add(user)
        db.session.commit()
        flash('Account Created, please sign in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'register', form = form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
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
        entry = Task(entry = form.entry.data, owner=current_user)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('toDo'))
    return render_template('toDoAdd.html', title = 'To-Do', form = form)

@app.route('/todo/<int:id>/delete', methods=['POST'])
def delete_tasks(id):
    task = db.session.query(Task).get_or_404(id)
    db.session.delete(task)
    db.session.commit()
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
    return render_template('mealLog.html', title = 'Meal Log', meals = meals)

@app.route('/meal-log/add', methods=['GET', 'POST'])
@login_required
def mealLogAdd():
    form = MealLogForm()
    if form.validate_on_submit():
        flash('Meal Added', 'success')
        meal = Meal(food=form.food.data, servings=form.servings.data, calories=form.calories.data, protein=form.protein.data, carbs=form.carb.data, fats=form.fat.data, owner=current_user)
        db.session.add(meal)
        db.session.commit()
        return redirect(url_for('mealLog'))
    return render_template('mealLogAdd.html', title = 'Meal Log', form = form)

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html', title = 'pomodoro timer')

@app.route('/journal/entry')
def entry():
    return render_template('entry.html', title = 'journal')
