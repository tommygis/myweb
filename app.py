# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 15:29
# @Author  : Zhao Zhufei
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
# def hello_world():
#     return 'Hello World'
@app.route('/hello/<name>')
def hello_world(name = None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
