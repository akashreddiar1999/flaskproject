# app/__init__.py

from flask import Flask
from flask_bootstrap import Bootstrap

# Initialize the app
app = Flask(__name__)
bootstrap = Bootstrap(app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

