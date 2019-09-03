#!/usr/bin/python
# coding=UTF-8
'''
@Author: recar
@Date: 2019-08-16 11:05:41
@LastEditTime: 2019-08-29 14:24:16
'''

from app import create_app

server = create_app()

if __name__ == "__main__":
    server.run("0.0.0.0",8080)