from flask import jsonify
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, \
    BadSignature
from app.models import User
import os

secret_key = os.environ.get("secret_key", "recar")

#返回token字符串
def generate_auth_token(uid, is_amdin=False, scope=None,
                        expiration=5000):
    #通过flask提供的对象，传入过期时间和flask的SECRET_KEY
    """生成令牌"""
    s = TimedJSONWebSignatureSerializer(secret_key,
                expires_in=expiration)
    #token里面的值，是技术方案需要订的，做相关的业务逻辑验证，uid唯一值表示当前请求的客户端
    #type表示客户端类型，看业务场景进行增删
    #scope权限作用域
    #设置过期时间，这个是必须的，一般设置两个小时
    return s.dumps({
        'uid': uid,
        'is_amdin': is_amdin,
        'scope':scope
    }).decode('ascii')

# token验证
def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    # except SignatureExpired:
    #     raise MyHttpAuthFailed('token expired')
    #     # return {'message': 'token expired'}, return_code.Unauthorized#token_expired() # valid token, but expired
    # except BadSignature:
    #     raise MyHttpAuthFailed('token invalid')
    #     # return {'message':'token invalid'}, return_code.Unauthorized #invalid_token()  # invalid token
    except:
        return None

    user = User.query.filter_by(id=data['uid']).first()
    return user