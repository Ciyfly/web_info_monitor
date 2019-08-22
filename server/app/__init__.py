import os
import sys
import logging
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import * 

app = Flask("server")


# 日志系统配置
handler = logging.FileHandler('server.log', encoding='UTF-8')
logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

# 读取配置文件
base_path = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(base_path, "config.py")
app.config.from_pyfile(config)

from app.utils import token_util

# flask-login
login_manager = LoginManager(app)
# set login view
login_manager.login_view = 'login'

# db
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# 设置允许跨域
# CORS(app, supports_credentials=True)
CORS(app)

from app.views import user

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)