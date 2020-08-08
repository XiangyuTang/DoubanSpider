#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/8/6 23:45
#@Author: XiangyuTang
#@File  : testWordCloud.py

import jieba #分词
from matplotlib import pyplot as plt #绘图，数据可视化
from wordcloud import WordCloud #词云
from PIL import Image #图片处理
import numpy as np #矩阵运算
import sqlite3 #数据库

#准备词云所需要的词
con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
	# print(item[0])
	text = text+item[0]
# print(text)
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(string)

#准备遮罩图片
img = Image.open(r'.\static\assets\img\Hepburn.jpg') #打开遮罩图片,注意图片背景色不能是透明色的png
img_array = np.array(img) #将图片转换为数组
wc = WordCloud(
	background_color='white', #设置背景色
	mask = img_array,
	font_path=r'C:\Users\16616\AppData\Local\Microsoft\Windows\Fonts\电影海报字体.ttf' #字体所在电脑的位置C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #不显示坐标轴

#输出词云图片到文件
plt.savefig(r'.\static\assets\img\wordcloud.jpg',dpi=600)
plt.show()