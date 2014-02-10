# -*- coding: utf-8 -*-
#第3セット(28) 各単語から文字バイグラムを抽出するプログラムを実装せよ．また，(27)と同様の方法で，頻度の高い文字バイグラムトップ100（バイグラムと頻度がソートされたもの）を作成せよ．
from collections import defaultdict
import sys
import re
#1行1単語形式のテキストを作った movie_reviews.txt.tok
fin = open('movie_reviews.txt.tok', 'r')

#word2bigram2freq（辞書型でバイグラム文字列と頻度を記録）
word2bigram2freq = defaultdict(int)
#バイグラム保持用変数
bigram = ['', '']
#ファイルを一行ずつ読み込み処理
for words in fin:
    words = words.rstrip('\n')
    #リストの大きさの取得を一回にすることで早い？（何回もlen(words)と書くよりも）
    wordslen = len(words)
    #1文字はバイグラムに含めない
    if wordslen == 1:
        continue
    #バイグラムの取得
    for elem_num in range(0, wordslen):
        if elem_num != 0 and elem_num != wordslen:
            word2bigram2freq[words[elem_num-1] + words[elem_num]] += 1
fin.close()

#頻度が大きい順にソートし、上位100件を表示
for k, v in sorted(word2bigram2freq.items(), key = lambda x:x[1], reverse = True)[:100]:
    print "%s\t%d" %(k, v)
