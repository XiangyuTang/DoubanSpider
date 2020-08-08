#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/31 23:37
#@Author: XiangyuTang
#@File  : Testxlwt.py

import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
worksheet = workbook.add_sheet("sheet1") #创建工作表单
worksheet.write(0,0,"hello")  #写入数据，参数1"行"，参数2"列"，参数3是内容
workbook.save("test.xls")  #保存数据表
'''

workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
worksheet = workbook.add_sheet("sheet1") #创建工作表单
for i in range(0,9):
	for j in range(0,i+1):
		worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save("test.xls")  #保存数据表