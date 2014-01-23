# -*- coding: utf-8 -*-
#第2セット(16)括弧表現のうち，括弧の内側がアルファベット大文字の文字列，括弧の左側が漢字の文字列のものを抽出せよ．このとき，括弧の左側の表現と括弧の内側の表現をタブ区切り形式で出力せよ．
import sys
import re

#自分のtwitterのつぶやきを１列に並べたものを利用
fin = open('mytweet2.txt', 'r')

#tlにはtwitterのtimelineを一行づつ挿入
tl = list()
line = fin.readline()
while line:
    tl.append(line.rstrip('\n'))
    line = fin.readline()

fin.close()

#正規表現をセットし検索、見つかったら表示
ReCompile = re.compile("[一-龠々]*\([A-Z]*\)")
for LineNum in range(len(tl)):
    if ReCompile.search(tl[LineNum]) != None:
        print tl[LineNum]
