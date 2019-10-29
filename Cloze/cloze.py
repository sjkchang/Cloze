from flask import Flask, render_template, url_for
import forms
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'b825c713da1c27fc72d8cb8d0875f7cc'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'login', form = form)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'register', form = form)

@app.route('/daily_planner')
def dailyPlanner():
    return render_template('dailyPlanner.html', title = 'Daily Planner')

@app.route('/workout_log')
def workoutLog():
    return render_template('workoutLog.html', title = 'Workout Log')

if __name__ == '__main__':
    app.debug = True
    app.run()
