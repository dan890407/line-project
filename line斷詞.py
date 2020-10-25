import jieba
from collections import Counter
import json
import os
original_files=os.listdir('./processed')
for i in original_files:
    before='./processed//'+i
    with open(before,"r",encoding="utf-8") as f:
        with open("data.txt","a+",encoding="utf-8")as p:
            for line in f.readlines():
                k=line.split(" ")
                if len(k)>2:
                    print (k[2:])
                    p.write('/'.join(k[2:])+'\n')
all_words = []
jieba.set_dictionary('dict.txt.big')
stopword_set = set()
with open('停用詞-繁體中文.txt','r', encoding='utf-8') as stopwords:
    for stopword in stopwords:
        stopword_set.add(stopword.rstrip('\n'))
with open('data.txt','r', encoding='utf-8') as sentences:
    for sentence in sentences:
        sentence = sentence.strip('\n')
        words = jieba.cut(sentence, cut_all=False)
        for word in words:
            if word not in stopword_set:
                all_words.append(word)
dict_words = dict(Counter(all_words))
items=list(dict_words.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
