# encoding = utf-8
import requests
from bs4 import BeautifulSoup
import os
import string
import jieba
import jieba.analyse
import csv
import codecs



url = 'https://governance.com/articles/'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', attrs={'class':'article-content'})
pic_link = content.find_all('h3')

for link in pic_link:
    a = link.find('a')['href']
    # 下載首頁內容
    r = requests.get(a)

    # 確認是否下載成功
    if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
        soup = BeautifulSoup(r.text, 'html.parser')

        # 以 CSS 的 class 抓出內容
        # 標題
        title = soup.select('.page-title')
        for t in title:
            print("Title: \n" + t.text)

        # 作者
        author = soup.select('.article-meta .post-meta .meta-author .author-name')
        for a in author:
            print("Author Name: \n" + a.text)

        # 日期
        date = soup.find('a', class_='post-time')
        for d in date:
            print("Date: \n" + d.text)

        # 內容
        content = soup.select('.article-content')
        for c in content:
            print("Content: \n " + c.text)

        file = open("C:/Users/IDEA3C/PycharmProjects/crawlers/txt/20180821-3.txt", 'w', encoding='UTF-8')
        file.writelines("Title: \n" + t.get_text() + "\n \n")
        file.writelines("Author Name: \n" + a.get_text() + "\n \n")
        file.writelines("Date: \n" + d.get_text() + "\n \n")
        file.writelines("Content: \n" + c.get_text())
        file.close()

        # stopkeyword = [line.strip() for line in open('stopwords.txt').readlines()]  # 将停止词文件保存到列表
        text = open(r"C:/Users/IDEA3C/PycharmProjects/crawlers/txt/20180821-3.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容
        zidian = {}
        fenci = jieba.cut_for_search(text)
        for fc in fenci:
            if fc in zidian:
                zidian[fc] += 1
            else:
                # zidian.setdefault(fc,1)   #字典中如果不存在键，就加入键，键值设置为1
                zidian[fc] = 1
        # 计算tfidf
        tfidf = jieba.analyse.extract_tags(text, topK=100, withWeight=True)

        # 写入到csv
        output = open(r'C:/Users/IDEA3C/PycharmProjects/crawlers/csv/20180821-3.csv', 'a')
        output.write('詞語,詞頻,詞權\n')
        for word_weight in tfidf:
            # if word_weight in stopkeyword:
            # pass
            # else:  # 不存在的话就输出
            print
            word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'
            output.write('%s,%s,%s\n' % (
                word_weight[0], zidian.get(word_weight[0], 'not found'), str(int(word_weight[1] * 100)) + '%'))
        output.close()

        #寫入到all
        output = open(r'C:/Users/IDEA3C/PycharmProjects/crawlers/all/allarticles.csv', 'a')
        output.write('文章代號,文章名稱,作者,日期,網址\n')


        os.rename(os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/txt/', '20180821-3.txt'), os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/txt/', t.get_text().replace(":"," ") + ".txt"))
        os.rename(os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/csv/', '20180821-3.csv'), os.path.join('C:/Users/IDEA3C/PycharmProjects/crawlers/csv/', t.get_text().replace(":"," ") + ".csv"))
