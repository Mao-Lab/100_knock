# coding: utf-8
import sys
from collections import Counter

#ファイル読み込み
fin = open('col2.txt', 'r')
line = fin.readline()

#ファイル内容をリストへ挿入
col2 = list()
while line:
    col2.append(line)
    line = fin.readline()
fin.close()

#文字列をカウントして、カウントが多い順に並べる
result = list()
result = Counter(col2).most_common()

for x in range(len(result)):
    print result[x][0],

#高性能なコンテナ・データ型のcollectionsを利用
#
#Counterオブジェクトのmost_commonを用いると
#カウントが多いものから少ないものまで順に並べたリストを返してくれる。
#
#回数も表示するとき
#for x in range(len(result)):
#    print "%s\t%s" %(result[x][0].rstrip("\n"),result[x][1])
