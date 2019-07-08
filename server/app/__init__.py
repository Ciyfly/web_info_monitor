from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask("server")

# flask-login
login_manager = LoginManager(app)
# set login view
login_manager.login_view = 'login'


# db
db = SQLAlchemy(app)

app.config.from_pyfile("config.py")

from app.views import index
