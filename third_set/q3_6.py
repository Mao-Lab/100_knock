# -*- coding: utf-8 -*-
#第3セット(26) -nessと-lyの両方の派生語尾をとる単語をすべて抜き出せ
import sys
import re

#1行1単語形式のテキストを作った movie_reviews.txt.tok
fin = open('movie_reviews.txt.tok', 'r')

#-nessと-lyが語尾となる正規表現
ReCompile = re.compile("((ness)|(ly))$")
#ファイルを一行ずつ読み込み
for word in fin:
    if ReCompile.search(word):
        print word,
fin.close()
