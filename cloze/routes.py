from cloze import app, db, bcrypt, login_manager
from flask import render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm, PlannerForm
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
            login_user(user, remember=False)
            return redirect(url_for('home'))
        flash('Email or Pasword is invalid', 'fail')
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

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')

@app.route('/daily_planner')
@login_required
def dailyPlanner():
    return render_template('dailyPlanner.html', title = 'Daily Planner')

@app.route('/daily_planner_edit', methods = ['GET', 'POST'])
@login_required
def dailyPlannerEdit():
    form = PlannerForm()
    if form.validate_on_submit():
        return redirect(url_for('dailyPlanner'))
    return render_template('dailyPlannerEdit.html', title = 'Daily Planner', form = form)

@app.route('/meal-log')
@login_required
def workoutLog():
    return render_template('mealLog.html', title = 'Meal Log')

@app.route('/pomodoro')
def about():
    return render_template('pomodoro.html', title = 'pomodoro timer')
