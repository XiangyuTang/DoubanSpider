#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/3 21:25
#@Author: XiangyuTang
#@File  : testFlask.py.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return '<h1>hhahahah Hello World</h1>'


if __name__ == '__main__':
	app.run(debug=True)
	app.run()