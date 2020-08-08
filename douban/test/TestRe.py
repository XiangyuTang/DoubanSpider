#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/30 11:57
#@Author: XiangyuTang
#@File  : TestRe.py

#正则表达式：字符串模式，判断字符串是否符合一定的标准

import re
#创建模式对象
pat = re.compile("AA") #此处的AA是正则表达式，用来匹配其他字符串
# m = pat.search("CAABA") #search字符串被校验的内容
# m = pat.search("AACBAAADDDAAA") #search方法进行比对查找

#没有模式对象
# m = re.search("asd","ABasdhh")  #简写，第一个参数是规则，后面是被考察的对象
# print(m)

# print(re.findall("a","AHknknaadv")) #前面字符串是规则，后面字符串是被校验的字符串

print(re.findall("[A-Z]","AHknknGadv"))
print(re.findall("[A-Z]+","AHknknGadv"))

#sub
print(re.sub("a","A","abcdcasd")) # 在abcdcasd中找到a，用A替换

#建议在正则表达式中，被比较的字符串前面加上r  ,不用担心转义字符的问题
a = r"\aadb-\'"
print(a)