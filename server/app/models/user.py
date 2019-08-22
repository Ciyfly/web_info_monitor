
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import datetime

class User(UserMixin, db.Model):
    """用户
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    invitation_code_id = db.Column(db.Integer, db.ForeignKey('invitation_code.id'))
    invitation_code = db.relationship('InvitationCode', foreign_keys=invitation_code_id)

    createtime = db.Column(db.DateTime, default=datetime.datetime.now())
    def __init__(self, name, password, email, is_admin, invitation_code):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.is_admin = is_admin
        self.invitation_code = invitation_code

    #定义一个验证密码的方法
    def check_password(self, rawpwd):
        return check_password_hash(self.password, rawpwd)

    def __repr__(self):
        return {
            username: self.username,
            email: self.email
        }



class InvitationCode(db.Model):
    """邀请码
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invitation_code = db.Column(db.String(32), unique=True, nullable=False)
    created_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.relationship('User', foreign_keys=created_id)
    user = db.relationship('User', foreign_keys=user_id)
