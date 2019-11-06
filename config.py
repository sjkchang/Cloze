import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    SECRET_KEY = 'b825c713da1c27fc72d8cb8d0875f7cc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(basedir, 'clozeApp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
