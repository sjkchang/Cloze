from flask import Flask, render_template, url_for, flash, redirect
import forms
from forms import LoginForm, RegistrationForm, PlannerForm

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'b825c713da1c27fc72d8cb8d0875f7cc'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You logged in', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title = 'login', form = form)

@app.route('/pomodoro')
def about():
    return render_template('pomodoro.html', title = 'pomodoro timer')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('You are registered', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'register', form = form)

@app.route('/daily_planner')
def dailyPlanner():
    return render_template('dailyPlanner.html', title = 'Daily Planner')

@app.route('/daily_planner_edit', methods = ['GET', 'POST'])
def dailyPlannerEdit():
    form = PlannerForm()
    if form.validate_on_submit():
        return redirect(url_for('dailyPlanner'))
    return render_template('dailyPlannerEdit.html', title = 'Daily Planner', form = form)

@app.route('/meal-log')
def workoutLog():
    return render_template('mealLog.html', title = 'Meal Log')


if __name__ == '__main__':
    app.debug = True
    app.run()
