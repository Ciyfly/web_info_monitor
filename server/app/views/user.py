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
    if User.query.filter(User.username == username).first() and \
        User.check_password_hash(password):
        data: {
            "Token": token_util.generate_auth_token()
        }
        response = success_response(data)
    else:
        response =  faild_response(20003)

    return response

@user_blueprint.route("/register/")
def register():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    email = request.form.get("email", "")
    invitation_code = request.form.get("invitation_code", "")
    db_invitation_code = InvitationCode.query.filter(InvitationCode.invitation_code == invitation_code).first()
    if db_invitation_code:
        user = User(
            username = username,
            password = password,
            email = email,
            invitation_code = invitation_code,
            is_admin = False
        )
        return jsonify({
            "message": "success", 
            "data":user
        })
    else:
        return jsonify({
            "message": "invitation code not found", 
            "data":[]
        })        

