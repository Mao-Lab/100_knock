# coding: utf-8
import sys

fin = open('col1.txt', 'r')
line = fin.readline()

col1 = set() #set型を用いてuniqにする

while line:
    col1.add(line) #すべての要素をset　col1に格納
    line = fin.readline()
fin.close()

print len(col1)

#コマンドでの確認
#sort col1.txt | uniq | wc -l
#1897
