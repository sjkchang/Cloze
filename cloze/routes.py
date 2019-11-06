from cloze import app, db, bcrypt, login_manager
from flask import render_template, url_for, flash, redirect, request
from forms import LoginForm, RegistrationForm, PlannerForm, TimerForm, UpdateAccountForm
from models import User
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
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

@app.route('/daily-planner')
@login_required
def dailyPlanner():
    return render_template('dailyPlanner.html', title = 'Daily Planner')

@app.route('/daily-planner-edit', methods = ['GET', 'POST'])
@login_required
def dailyPlannerEdit():
    form = PlannerForm()
    if form.validate_on_submit():
        return redirect(url_for('dailyPlanner'))
    return render_template('dailyPlannerEdit.html', title = 'Daily Planner', form = form)

@app.route('/meal-log')
@login_required
def mealLog():
    return render_template('mealLog.html', title = 'Meal Log')

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html', title = 'pomodoro timer')
