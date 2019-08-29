#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-08-29 10:39:42
@LastEditTime: 2019-08-29 17:42:43
'''

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import InvitationCode, User