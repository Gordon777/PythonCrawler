#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os


# 下載Yahoo首頁內容
r = requests.get('https://governance.com/insurance-not-commodity/')

#確認是否下載成功
if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    # 以 CSS 的 class 抓出內容
    #標題
    title = soup.select('.page-title')
    for t in title:
        print("Title: \n" + t.text)

    #作者
    author = soup.select('.article-meta .post-meta .meta-author .author-name')
    for a in author:
        print("Author Name: \n" + a.text)

    #日期
    date = soup.find('a', class_='post-time')
    for d in date:
        print("Date: \n" + d.text)

    #內容
    content =  soup.select('.article-content')
    for c in content:
        print("Content: \n " + c.text)

file = open("C:/Users/IDEA3C/PycharmProjects/crawlers/20180821-3.txt",'w',encoding='UTF-8')
file.writelines("Title: \n" + t.get_text() + "\n \n")
file.writelines("Author Name: \n" + a.get_text() + "\n \n")
file.writelines("Date: \n" + d.get_text() + "\n \n")
file.writelines("Content: \n" + c.get_text())
file.close()

os.rename(os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/' , '20180821-3.txt'), os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/' , t.get_text() + ".txt"))



