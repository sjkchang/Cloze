from app import clozeApp
from flask import render_template, url_for, flash, redirect
import forms
from forms import LoginForm, RegistrationForm, PlannerForm


@clozeApp.route('/home')
def home():
    return render_template('home.html')

@clozeApp.route('/', methods = ['GET', 'POST'])
@clozeApp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You logged in', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title = 'login', form = form)

@clozeApp.route('/pomodoro')
def about():
    return render_template('pomodoro.html', title = 'pomodoro timer')

@clozeApp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('You are registered', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'register', form = form)

@clozeApp.route('/daily_planner')
def dailyPlanner():
    return render_template('dailyPlanner.html', title = 'Daily Planner')

@clozeApp.route('/daily_planner_edit', methods = ['GET', 'POST'])
def dailyPlannerEdit():
    form = PlannerForm()
    if form.validate_on_submit():
        return redirect(url_for('dailyPlanner'))
    return render_template('dailyPlannerEdit.html', title = 'Daily Planner', form = form)

@clozeApp.route('/meal-log')
def workoutLog():
    return render_template('mealLog.html', title = 'Meal Log')
