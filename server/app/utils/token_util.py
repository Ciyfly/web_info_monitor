from app.config import SECRET_KEY
from flask import jsonify
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, \
    BadSignature

#返回token字符串
def generate_auth_token(uid, is_amdin, scope=None,
                        expiration=5000):
    #通过flask提供的对象，传入过期时间和flask的SECRET_KEY
    """生成令牌"""
    s = TimedJSONWebSignatureSerializer(SECRET_KEY,
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