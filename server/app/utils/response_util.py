#!/usr/bin/python
# coding=UTF-8
'''
@Author: ysy
@Date: 2019-08-29 12:13:21
@LastEditTime: 2019-08-29 18:17:55
'''
from flask import make_response, jsonify

status_code_em = {
    20003: "用户名或密码不正确",
    20004: "注册数据违法不能为空",
    20005: "邀请码不正确"
}
def success_response(data):
    response = make_response(
        jsonify({
            "message": "success",
            "data": data
        })
    )
    response.status = str(200)
    return response

def faild_response(status_code):
    response = make_response(
        jsonify({
            "message": status_code_em[status_code],
            "data": {}
        })
    )
    response.status = str(status_code)
    return response

