# -*- coding: utf-8 -*-
#第2セット(18)仙台市の住所らしき表現にマッチする正規表現を各自で設計し、抽出せよ
import sys
import re

#仙台市の住所らしき表現を入れたものを挿入した、自分のtweetを利用
fin = open('mytweet3.txt', 'r')

#tlにはtwitterのtimelineを一行づつ挿入
tl = list()
line = fin.readline()
while line:
    tl.append(line.rstrip('\n'))
    line = fin.readline()

fin.close()

#正規表現をセットし検索、見つかったら表示
#仙台市の住所は　仙台市**区**である
ReCompile = re.compile("仙台市[一-龠々A-Z]*区[一-龠々A-Z]*")
for LineNum in range(len(tl)):
    SearchResult = ReCompile.search(tl[LineNum])
    if SearchResult != None:
        print SearchResult.group()
