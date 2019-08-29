#!/usr/bin/python
# coding=UTF-8
'''
@Author: ysy
@Date: 2019-08-29 12:13:21
@LastEditTime: 2019-08-29 18:57:34
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
            "status_code": 2000,
            "message": "success",
            "data": data
        })
    )
    return response

def faild_response(status_code):
    response = make_response(
        jsonify({
            "status_code": status_code,
            "message": status_code_em[status_code],
            "data": {}
        })
    )
    return response

