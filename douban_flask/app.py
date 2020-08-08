#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/4 19:28
#@Author: XiangyuTang
#@File  : app.py.py

from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/index')
def home():
	# return render_template('index.html')
	return index()

@app.route('/movie')
def movie():
	datalist = []
	conn = sqlite3.connect("movie.db")
	cur = conn.cursor()
	sql = "select * from movie250"
	data = cur.execute(sql)
	for item in data:
		datalist.append(item)
	cur.close()
	conn.close()
	return render_template("movie.html",datalist = datalist)
@app.route('/team')
def team():
	return render_template("team.html")
@app.route('/word')
def word():
	return render_template("word.html")
@app.route('/score')
def score():
	score = [] #评分多少种，echarts的x坐标
	movie_num = [] #电影多少个，echarts的y坐标
	conn = sqlite3.connect("movie.db")
	cur = conn.cursor()
	sql = "select score,count(score) from movie250 group by score"
	data = cur.execute(sql)
	for item in data:
		score.append(item[0])
		movie_num.append(item[1])
	cur.close()
	conn.close()
	return render_template("score.html",score = score,movie_num=movie_num)

if __name__ == '__main__':
	app.run(debug=True)