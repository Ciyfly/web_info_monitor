#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-08-29 10:41:17
@LastEditTime: 2019-09-03 18:02:47
'''

from flask import Blueprint
user_blueprint = Blueprint('user',__name__)
domain_blueprint = Blueprint('domain',__name__)

from .user import *
from .domain import *