# -*- coding: utf-8 -*-
#第3セット(27) (10)のプログラムを呼び出すことで、頻度の高い英単語トップ100(単語と頻度がソートされたもの)を作成せよ
from collections import defaultdict
import sys

#1行1単語形式のテキストを作った movie_reviews.txt.tok
fin = open('movie_reviews.txt.tok', 'r')

word2freq = defaultdict(int)
#ファイルを一行ずつ読み込み
for word in fin:
    word = word.rstrip('\n')
    word2freq[word] += 1
fin.close()

i = 1
for k,v in sorted(word2freq.items(), key = lambda x:x[1], reverse = True):
    if i <= 100:
        print "%s\t%d" %(k,v)
    i = i + 1
