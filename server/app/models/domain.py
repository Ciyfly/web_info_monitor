#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-09-03 18:05:56
@LastEditTime: 2019-09-03 19:41:04
'''

from . import db, user_domain
import datetime

class Domain(db.Model):
    """ 域名
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    # 子域名指向主域名的id
    parent_id = db.Column(db.Integer, default=0)
    users = db.relationship('User',
                            secondary=user_domain,
                            back_populates='domains')

    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "domain": self.domain,
            "parent_id": self.parent_id
        })