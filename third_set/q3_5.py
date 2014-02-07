# -*- coding: utf-8 -*-
#第3セット(25) (24)の出力を標準入力から1行(1単語)を読みこむごとに、その単語を小文字に変換した文字列を各行の最終列にタブ区切り形式で追加し、標準出力に書き出せ
import sys

fin = open('movie_reviews.txt', 'r')

#ファイルを一行ずつ読み込み
for words in fin:
    words = words.rstrip('\n')  #改行コードを削除
    words = words.split() #単語で分割する

    for word in words:
        print "%s\t%s" %(word,word.lower())
    print ''
fin.close()
