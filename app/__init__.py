from flask import Flask
from config import Config

clozeApp = Flask(__name__)
clozeApp.config.from_object(Config)

from app import routes
