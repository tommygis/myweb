# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 15:29
# @Author  : Zhao Zhufei
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/nihao')
def hello_user():
    return 'nihao'

if __name__ == '__main__':
    app.run()