#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-08-29 10:41:17
@LastEditTime: 2019-08-29 11:21:41
'''

from flask import Blueprint
user_blueprint = Blueprint('user',__name__)

from .user import *