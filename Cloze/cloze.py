from flask import Flask, render_template, url_for

# uncomment line below once you have created the
# TopCities class inside the form.py file

app = Flask(__name__)
app.debug = False
#app.config['SECRET_KEY'] = 'some-key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html', title = 'login')

if __name__ == '__main__':
    app.debug = True
    app.run()
