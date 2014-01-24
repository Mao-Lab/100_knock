# -*- coding: utf-8 -*-
#第2セット(17)人名らしき表現にマッチする正規表現を各自で設計し、抽出せよ
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
#人名の正規表現を 日本語or英語 + さんorちゃんorくんor君　と設計
ReCompile = re.compile("[一-龠々A-Z]*(さん|ちゃん|くん|君)")
for LineNum in range(len(tl)):
    SearchResult = ReCompile.search(tl[LineNum])
    if SearchResult != None:
        print SearchResult.group()
