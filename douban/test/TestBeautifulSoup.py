#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/29 22:32
#@Author: XiangyuTang
#@File  : TestBeautifulSoup.py

'''
BeautifulSoup4 将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''
from bs4 import BeautifulSoup #网页解析，获取数据

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# print(bs.a)  #找到第一个a标签，并打印标签内所有的内容
# print(bs.head)
# print(type(bs.head))   #输出<class 'bs4.element.Tag'>
# 1.Tag 标签及其内容：只能拿到他所找到的第一个内容↑↑↑

# print(bs.title)
# print(bs.title.string)
# print(type(bs.title.string)) #输出<class 'bs4.element.NavigableString'>
# 2.NavigableString  标签里的内容（字符串）↑↑↑

# print(bs.a.attrs)  #输出{'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
#可以快速拿到标签里的属性↑↑↑↑↑↑

# print(type(bs)) #输出<class 'bs4.BeautifulSoup'>
# print(bs.name)
# 3.BeautifulSoup  表示整个文档,即就是bs对象↑↑↑↑↑↑

# print(bs.a.string)
# print(type(bs.a.string)) #输出 <class 'bs4.element.Comment'>
# 4.是一个特殊的NavigableString，输出的内容不包含注释符号


# ------------------------------------------------------------
# 文档的遍历
# print(bs.head.contents) #获取head标签里的元素集合，返回一个列表
# print(bs.head.contents[1])
#更多内容，搜索文档

# 文档的搜索
# 1) find_all()
# 字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all("a") #找到所有a标签

# 2）search() 正则表达式搜索
import re
# t_list= bs.find_all(re.compile("a")) #包含“a”内容的标签，非完全匹配


# 3）传入一个函数/方法，根据函数的要求来搜索
# def name_is_exists(tag):
# 	return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
# 	print(item)

# print(t_list)

# 2.kwargs   参数 我就想找到谁，id,name,href....
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_ = True)
# t_list = bs.find_all(href="http://news.baidu.com")
# for item in t_list:
# 	print(item)

# 3. text 参数
# t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text = ["hao123","地图","贴吧"])
# t_list= bs.find_all(text = re.compile("\d"))  #应用正则表达式来插好包含特定文本的内容（标签里的字符串）


# 4. limit参数
# t_list = bs.find_all("a",limit = 3)
# for item in t_list:
# 	print(item)


#CSS 选择器
# t_list = bs.select("title")  #通过标签来查找
# t_list = bs.select(".mnav") #类名查找
# t_list = bs.select("#u1") #id查找
# t_list = bs.select("a[class='bri']") #带特定属性条件的标签查找
t_list = bs.select("head > title") #通过 > 父子标签查找
t_list = bs.select(".mnav ~ .bri") #通过 ~ 兄弟标签查找
print(t_list[0].get_text())
# for item in t_list:
# 	print(item)