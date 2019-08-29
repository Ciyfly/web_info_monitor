import os
import sys
import logging
from flask import Flask
from flask_login import LoginManager
from app.models import db
from flask_migrate import Migrate
from flask_cors import *
from app.views import user_blueprint

# db迁移
migrate = Migrate()


def create_app():
    app = Flask("server")
    # 读取配置文件
    base_path = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(base_path, "config.py")
    app.config.from_pyfile(config)
    # 设置允许跨域
    # cors.init_app(app, allow_headers='*')
    CORS(app, supports_credentials=True)
    # 日志系统配置
    handler = logging.FileHandler('server.log', encoding='UTF-8')
    logging_format = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    from logging.handlers import RotatingFileHandler 
    handler = RotatingFileHandler("flask.log", maxBytes=1024000, backupCount=10)
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    # db
    db.init_app(app)

    migrate.init_app(app, db)
    # 注册蓝图
    # app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(user_blueprint, url_prefix='/user')
    return app
