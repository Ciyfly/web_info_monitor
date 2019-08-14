import os
import sys
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask("server")

# flask-login
login_manager = LoginManager(app)
# set login view
login_manager.login_view = 'login'


# db
db = SQLAlchemy(app)
base_path = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(base_path, "config.py")
app.config.from_pyfile(config)

from app.views import index
