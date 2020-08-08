#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/1 17:48
#@Author: XiangyuTang
#@File  : TestSqlite.py

import sqlite3

conn = sqlite3.connect("test.db") #打开或者创建数据库文件
print("Opened database successfully.")

c = conn.cursor() #获取游标
# sql = '''
# 	create table company
# 		(id int paimary key not null,
# 		name text not null,
# 		age int not null,
# 		address char(50),
# 		salary real);
# '''
# c.execute(sql) #执行sql
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库连接
# print("Created table successfully.")

#3.插入数据
insert_sql1 = '''
	insert into company (id,name,age,address,salary)
	values(1,'张三',32,'北京',3000)
'''
c.execute(insert_sql1) #执行sql
insert_sql2 = '''
	insert into company (id,name,age,address,salary)
	values(2,'张三',32,'北京',6000)
'''
c.execute(insert_sql2) #执行sql
conn.commit() #提交数据库操作


#4.查询数据
sql = "select id,name,age,address,salary from company"
cursor = c.execute(sql)

for row in cursor:
	print("id=",row[0])
	print("name=", row[1])
	print("age=", row[2])
	print("adress=", row[3])
	print("salary=", row[4])

print("selected successfully.")
conn.close() #关闭数据库连接