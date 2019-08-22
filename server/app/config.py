#!/usr/bin/python
# coding=UTF-8
'''
@Author: Recar
@Date: 2019-08-16 11:05:41
@LastEditTime: 2019-08-22 14:35:34
'''
import os
from app import app

try:
    mysql_username = os.environ["mysql_username"]
    mysql_password = os.environ["mysql_password"]
    SQLALCHEMY_DATABASE_URI = f'mysql://{mysql_username}:{mysql_password}@127.0.0.1:3306/web_info_monitor?charset=utf8'
except Exception as e:
    app.logger.debug("需要在 server目录下创建 .env文件并写入 mysql用户名密码 否则使用sqlite")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///app.db'

app.logger.debug(f"使用数据库: {SQLALCHEMY_DATABASE_URI}")
SQLALCHEMY_TRACK_MODIFICATIONS = True
