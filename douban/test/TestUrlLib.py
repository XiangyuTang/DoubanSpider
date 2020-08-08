#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/29 20:02
#@Author: XiangyuTang
#@File  : TestUrlLib.py

import urllib.request

#获取一个get请求
# reponse = urllib.request.urlopen("https://fund.eastmoney.com/")
# print(reponse.read().decode("utf-8"))  # 对获取到的网页源码进行utf-8的解码

#获取一个post请求,模拟用户登录等场景
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


# 超时处理
import urllib.error
# try:
# 	response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1) #允许超时0.1s
# 	print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
# 	print("time out:  ",e)

#查看请求头部信息
# response = urllib.request.urlopen("http://www.baidu.com") #允许超时0.1s
# print(response.status) #返回状态码，如200，404
# print(response.getheaders()) #返回请求头部所有的信息
# print(response.getheader("server")) #返回请求头部中server的信息

#把自己伪装成浏览器
# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# headers = {
# 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"txy"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#把自己伪装成浏览器,访问豆瓣
url = "https://www.douban.com"
# url = "http://httpbin.org/post"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
# 构造请求对象
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))