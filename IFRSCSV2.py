#encoding = utf8

import jieba
import jieba.analyse  # 导入结巴jieba相关模块
import jieba.posseg as pseg

output = open(r'C:/ACLProject/ACL/TM/result1.csv', 'a')
output.write('詞語,詞性\n')
#stopkeyword = [line.strip() for line in open('stopwords.txt').readlines()]  # 将停止词文件保存到列表
text = open(r"C:/ACLProject/ACL/TM/tifrs-note_value.txt", "r", encoding="utf-8-sig").read()  # 导入需要计算的内容
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

# 分析詞性
words = pseg.cut(text)


# 写入到csv
for word,flag in words:
        print('%s,%s' %( word, flag))
        output.write('%s,%s\n' % (
            word, flag))

output.close()