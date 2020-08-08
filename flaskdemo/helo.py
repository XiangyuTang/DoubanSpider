#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/3 21:32
#@Author: XiangyuTang
#@File  : helo.py

from flask import Flask,render_template,request  #render_template是渲染的模板
import datetime
app = Flask(__name__)


#路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():
# 	return '<h1>hhahah123ah Hello World</h1>'


@app.route('/index')
def index():
	return '<h1>This is an index page.</h1>'

@app.route('/user/<name>') #传入路径中的字符串参数name
def welcome(name):
	return '<h1>hello!%s</h1>'%name

@app.route('/user/<int:id>') #传入路径中的整型参数id  ,此外还有float类型
def welcome2(id):
	return '<h1>hello!your id is %d</h1>'%id

#***注意***： 路由不能重复，用户通过位意的路径访问特定的函数

#返回给用户渲染后的网页文件
# @app.route("/")
# def index2():
# 	return render_template("index.html") #从templates文件夹里返回网页index.html,注意只能从templates文件夹

#向页面传递一个变量
@app.route("/")
def index2():
	time = datetime.date.today()
	name = ["s1","s2","s3","s4"]
	task = {"任务":"做作业","目标":"拿满分"}
	return render_template("index.html",var = time,list = name,task = task) #从templates文件夹里返回网页index.html,注意只能从templates文件夹


#表单提交
@app.route('/test/register')
def register():
	return render_template("form_files/register.html")

#接收表单提交的路由，需要指定method为post,否则报错Method Not Allowed
@app.route('/result',methods=['POST','GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template("form_files/result.html",result=result)



if __name__ == '__main__':
	app.run(debug=True) #调试模式，只用每次保存后就能更新
	# app.run() #非调试模式，每次更改代码，需要重启服务器才能更新