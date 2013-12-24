# coding: utf-8
import sys

def open_txt(file_name): #readlines関数を使用して、テキストファイルを読み出し
    f = open(file_name)
    line = f.readlines()
    f.close()
    return line

f1 = open_txt('col1.txt') #ファイルをオープン
f2 = open_txt('col2.txt')

i = 0 #f2の要素指定のために定義
for line in f1:
    print line.rstrip() + '\t' + f2[i].rstrip() #各要素には\nが末尾に含まれるためそれを除去し、print
    i = i + 1

