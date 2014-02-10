# -*- coding: utf-8 -*-
#第3セット(23)(22)の出力を標準入力から1行(1文)を読みこむごとに、スペースで単語列に分割し、1行1単語形式で標準出力に書き出せ。文の終端を表すため、文が終わるごとに空行を出力せよ
import sys
import re
fin = open('movie_reviews.txt', 'r')

ReCompile = re.compile('[A-Za-z\']')
#ファイルを一行ずつ読み込み
for words in fin:
    words = words.rstrip('\n')  #改行コードを削除
    words = words.split() #単語で分割する

    for word in words:
        if ReCompile.match(word):
            print word.lower()
fin.close()

#記号はどうするのかわからない。このプログラムだと
#記号も1単語として見てしまう。
