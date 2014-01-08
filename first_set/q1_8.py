# -*- coding: utf-8 -*-
import sys

fin = open('address.txt', 'r') #ファイルオープン
list=[] #リストを作成

line = fin.readline()
while line: #リストをタブで区切りながら読み込み
    list.append(line.split('\t'))
    line = fin.readline()
fin.close()

#リストの2つめの要素でソート
for x, y in sorted(list, key = lambda x:x[1], reverse = False):
    print x + '\t' + y,


#コマンドでの確認
# sort -t "       " -k 2 address.txt > 1_8_2.csv
