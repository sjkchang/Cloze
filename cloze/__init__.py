from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app(testing):
    app = Flask(__name__, instance_relative_config=False)

    if testing == False:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.TestConfig')

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        # Include our routes
        from . import routes

        db.create_all()

        return app

app = create_app(False)

