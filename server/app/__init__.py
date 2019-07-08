from flask import Flask

app = Flask("server")

from app.views import index
