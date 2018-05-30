# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 14:34
# @Author  : Skyling
# @File    : cartoon.py
# @Software: PyCharm

from bs4 import BeautifulSoup
#bs4版本 3已经放弃维护
import requests,os


url = 'https://xkcd.com/'

name = 'cartoon'
#本地文件夹创建
os.makedirs(name,exist_ok=True)

while not url.endswith('#'):#路径以#hash结束
    html = requests.get(url).text
    #设置解析器  htmlparser lxml
    soup = BeautifulSoup(html,'html.parser')
    comicUrl = soup.select('#comic img ') #搜索文档
    if comicUrl==[]:
        print('没有找到漫画')
    else:
        comicImageUrl = 'https:'+comicUrl[0].get('src')
        print('图像下载的路径',comicImageUrl)
        response = requests.get(comicImageUrl)#请求最后元素图片数据 sql 本地保存
        file_name = os.path.basename(comicImageUrl) #返回文件名字基本的文件名
        imageFile = open(os.path.join(name,file_name),'wb') #读取二进制模式打开文件夹获取图片
        for image in response.iter_content(1000):#遍历响应图片文件
            #每次遍历的文件写入文件目录中
            imageFile.write(image)
            #关闭I/O
        imageFile.close()

    pre_link = soup.select('a[rel="prev"]')[0].get('href')
    #请求前一页面是否有
    url ='https://xkcd.com/' + pre_link