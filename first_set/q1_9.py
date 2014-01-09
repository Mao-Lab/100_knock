# -*- coding: utf-8 -*-
import sys

fin = open('address.txt', 'r') #ファイルオープン
list=[] #リストを作成

line = fin.readline()
while line: #リストをタブで区切りながら読み込み
    list.append(line.split('\t'))
    line = fin.readline()
fin.close()

#リストの2カラム目、1カラム目の順でソート
for x, y in sorted(list, key = lambda x:(x[0],x[1]), reverse = True):
    print x + '\t' + y,

