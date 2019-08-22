from app import app
from flask import request, jsonify
from app.models.user import User, InvitationCode
from app import token_util

@app.route("/user/login", methods=['POST'])
def login():
    data = request.get_data()
    app.logger.debug(data)
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    app.logger.debug(f"usernmae: {username} password: {password}")
    if User.query.filter(User.username == username).first() and \
        User.check_password_hash(password):
        return jsonify({
            "message": "success",
            "data": {
                "Token": token_util.generate_auth_token()
            }
        })

@app.route("/user/register")
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

