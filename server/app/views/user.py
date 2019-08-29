from flask import request, jsonify, current_app
from app.models.user import User, InvitationCode
from . import user_blueprint
from app.utils import token_util
from app.utils.response_util import success_response, faild_response
# from app.__init__ import logger
import json

@user_blueprint.route("/login/", methods=['POST'])
def login():
    data = json.loads(request.get_data())
    username = data.get("username", "")
    password = data.get("password", "")
    current_app.logger.debug(f"usernmae: {username} password: {password}")
    user = User.query.filter(User.username == username).first()
    current_app.logger.debug(f"user: {user}")

    if user and  user.check_password(password):
        data: {
            "Token": token_util.generate_auth_token()
        }
        response = success_response(data)
    else:
        response =  faild_response(20003)

    return response

@user_blueprint.route("/register/")
def register():
    data = json.loads(request.get_data())
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    invitation_code = data.get("invitation_code")
    if username is None or password is None or email is None or invitation_code is None:
        return faild_response(2004)

    db_invitation_code = InvitationCode.query.filter(InvitationCode.invitation_code == invitation_code).first()
    if db_invitation_code:
        user = User(
            username = username,
            password = password,
            email = email,
            invitation_code = invitation_code,
            is_admin = False
        )
        return success_response(str(user))
    else:
        return faild_response(20005)

