#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-08-29 10:39:42
@LastEditTime: 2019-09-03 19:47:57
'''

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

user_domain = db.Table('user_domain',
db.Column('user_id', db.ForeignKey('user.id'), primary_key=True),
db.Column('domain_id', db.ForeignKey('domain.id'), primary_key=True)
)
from .user import InvitationCode, User
from .domain import Domain
