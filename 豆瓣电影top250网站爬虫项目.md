# 豆瓣电影top250网站爬虫项目

- 学习来源：https://www.bilibili.com/video/BV12E411A7ZQ

- 本仓库完全按照以上网站教程进行学习和搭建，感谢IT私塾李巍老师
- 涉及技术：
  - 爬虫：Python、Urllib(获取链接)、BeautifulSoup（将爬下来的HTML网页进行解析）、RE正则表达式（用于提取网页标签信息，即我们需要的数据）、Sqlite（数据库相关）
  - 网页可视化展示：Flask网页框架、Echarts、wordcloud
- 仓库主要内容：
  - douban：爬虫项目，针对[豆瓣电影top250](https://movie.douban.com/top250)网站爬取电影的详细信息，存入sqlite数据库、excel表格
  - douban_flask：将douban爬虫生成的数据库以网页进行展示（基于Flask框架、Echarts、WordCloud）
  - flask_demo：主要介绍Flask网页框架的开发流程，用法