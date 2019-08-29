#!/usr/bin/python
# coding=UTF-8
'''
@Author: Recar
@Date: 2019-08-29 16:45:05
@LastEditTime: 2019-08-29 18:01:56
'''
import uuid
from app.models import InvitationCode, db, User
# from flask import current_app
from app import create_app
app = create_app()

app.app_context().push()

def generate_admin():
    admin = User(
        username="admin", password="admin",
        email="admin@admin", is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    return admin
        
def generate_invitationcode():
        invitationcode = str(uuid.uuid1()).replace("-", "")
        current_app.logger.info(f"生成邀请码: {invitationcode}")
        invitationcode =  InvitationCode(
            invitation_code=invitationcode
            )
        db.session.add(invitationcode)
        db.session.commit()
        return invitationcode