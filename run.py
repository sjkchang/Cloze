#import os
#basedir = os.path.abspath(os.path.dirname(__name__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(basedir, 'app.db')
#SQLALCHEMY_TRACK_MODIFICATIONS = False
from app import clozeApp

if __name__ == '__main__':
    clozeApp.debug = True
    clozeApp.run()
