# -*- coding: utf-8 -*-
#第3セット(27) (10)のプログラムを呼び出すことで、頻度の高い英単語トップ100(単語と頻度がソートされたもの)を作成せよ
from collections import defaultdict
import sys
import re
#1行1単語形式のテキストを作った movie_reviews.txt.tok
fin = open('movie_reviews.txt.tok', 'r')


word2freq = defaultdict(int)
#ファイルを一行ずつ読み込み
head = 0
tail = 0
bigram = ['', '']
for word in fin:
    word = word.rstrip('\n')
    bigram[1] = bigram[0]
    bigram[0] = word
    bgmkey = bigram[1] + '\t' + bigram[0]

    if bigram[1] == '':
        head = 1
    else:
        head = 0

    if bigram[0] == '':
        tail = 1
    else:
        tail = 0

    if head == 0 and tail == 0:
#        print bgmkey
        word2freq[bgmkey] += 1
fin.close()

for k, v in sorted(word2freq.items(), key = lambda x:x[1], reverse = True)[:100]:
    print "%s\t%d" %(k, v)
