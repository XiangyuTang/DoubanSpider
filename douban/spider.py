#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/29 19:45
#@Author: XiangyuTang
#@File  : spider.py

from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error #指定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
	baseurl = "https://movie.douban.com/top250?start="
	# 1.爬取网页,获取数据
	datalist = getData(baseurl)
	# 3.保存数据
	savepath = "豆瓣电影top250.xls"
	dbpath = "movie.db"
	# saveData(datalist,savepath)
	saveData2DB(datalist,dbpath)

#全局变量，正则表达式的规则
findlink = re.compile(r'<a href="(.*?)">') #创建正则表达式的对象，表示一种匹配规则：快速找到电影链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #获取影片中图片的链接，re.S表示忽略字符中的换行符
findTitle = re.compile(r'<span class="title">(.*)</span>')
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findCommentNum = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')#一句话评价该电影
findBd = re.compile(r'<p class="">(.*?)</p>',re.S) #找到影片的相关内容


#爬取网页
def getData(baseUrl):
	datalist = []
	for i in range(0,10): #调用获取页面信息的函数10次
		url = baseUrl + str(i*25) #每次获取25条
		html = askURL(url) #保存获取到的网页源码

		#2. 逐一解析数据
		soup = BeautifulSoup(html,"html.parser")# 将抓取的html网页转换为树形结构的文档
		for item in soup.find_all('div',class_="item"): #查找符合要求的字符串，形成列表
			# print(item) #<div class="item">查看电影item的全部信息
			data = [] #保存一部电影的所有信息
			item = str(item) #转为字符串，用于正则表达式
			# print(item)

			# 影片的详情内容
			link = re.findall(findlink,item)[0] #re库通过正则表达式findlink查找指定字符串item
			# print(link)
			data.append(link)

			imgSrc = re.findall(findImgSrc,item)[0]
			data.append(imgSrc)

			title = re.findall(findTitle,item) #片名可能只有一个，没有外国名
			if(len(title)==2):
				chinese_title = title[0]
				data.append(chinese_title) #添加电影中文名
				foreign_title = title[1].replace("/","") #去掉无关的符号
				foreign_title = re.sub(r'\xa0',"",foreign_title)
				data.append(foreign_title) #添加电影外国名
			else:
				data.append(title[0])
				data.append(" ") #外文名留空，因为excel需要占位

			score = re.findall(findScore,item)[0]
			data.append(score)

			comment_num = re.findall(findCommentNum,item)[0]
			data.append(comment_num)

			inq = re.findall(findInq,item) #添加概述
			if(len(inq)!=0):
				inq = inq[0].replace("。","") #去掉句号
				data.append(inq)
			else:
				data.append(" ") #留空占位

			bd = re.findall(findBd,item)[0]
			bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) #去掉<br\>
			bd = re.sub('/'," ",bd)
			bd = re.sub('\xa0', " ", bd)
			data.append(bd.strip()) #去掉前后的空格bd.strip()

			datalist.append(data)  #把处理好的一条电影信息放入list
	print(datalist)
	return datalist


# 得到一个指定URL的网页内容
def askURL(url):
	#head主要是伪装作用，用户代理，告诉豆瓣服务器，我们是什么类型的浏览器
	# 本质上是告诉浏览器我们可以接收什么类型的文件内容
	head={
		"User-Agent":" Mozilla / 5.0(Windows NT 10.0;	Win64;	x64;	rv: 78.0) Gecko / 20100101	Firefox / 78.0"
	}
	request = urllib.request.Request(url,headers=head)
	html = ""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode("utf-8")
		# print(html)
	except urllib.error.URLError as e:
		if(hasattr(e,"code")):
			print(e.code)
		if(hasattr(e,"reason")):
			print(e.reason)
	return html

#保存数据
def saveData(datalist,savepath):
	print("saving...")
	book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
	sheet = book.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)  # 创建工作表单

	col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数量","概况","相关信息")
	for i in range(0,8):
		sheet.write(0,i,col[i]) #写一行列名
	for i in range(0,250):
		print("第%d条."%(i+1))
		data = datalist[i]
		for j in range(0,8):
			sheet.write(i+1,j,data[j])

	book.save(savepath)  # 保存数据表
	print("saved.")

def saveData2DB(datalist,dbpath):
	init_db(dbpath)
	conn = sqlite3.connect(dbpath)
	cur = conn.cursor()
	for data in datalist:
		for index in range(len(data)): #data的列
			data[index] = '"'+data[index]+'"'
		sql = '''
			insert into movie250
			(info_link,pic_link,cname,ename,score,rated,introduction,info)
			values(%s)'''%",".join(data)
		print(sql)
		cur.execute(sql)
		conn.commit()
	cur.close()
	conn.close()

def init_db(dbpath):
	sql = '''
		create table movie250
		(
			id integer primary key autoincrement,
			info_link text,
			pic_link text,
			cname varchar,
			ename varchar,
			score numeric,
			rated numeric,
			introduction text,
			info text
		)
	''' #创建数据表
	conn = sqlite3.connect(dbpath)  #如果路径存在就链接，不存在就创建
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

if __name__ == "__main__":
	main()
	# init_db("movietest.db")
	# askURL("https://movie.douban.com/top250")
