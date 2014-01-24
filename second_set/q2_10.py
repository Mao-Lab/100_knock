# -*- coding: utf-8 -*-
#第2セット(20)ツイートから絵文字らしき文字列を抽出せよ
import sys
import re

#自分のtweetを利用、絵文字は含まれていない
fin = open('mytweet3.txt', 'r')

#tlにはtwitterのtimelineを一行づつ挿入
tl = list()
line = fin.readline()
while line:
    tl.append(line.rstrip('\n'))
    line = fin.readline()

fin.close()

#正規表現をセットし検索、見つかったら表示
#docomoの絵文字をセット
ReCompile = re.compile("\([\ue63e-\ue6a5\ue6ac-\ue6ae\ue6b1-\ue6ba\u6ce-\u757]\)")
for LineNum in range(len(tl)):
    SearchResult = ReCompile.search(tl[LineNum])
    if SearchResult != None:
        print SearchResult.group()
