# coding: utf-8
import sys

fin1 = open('col1.txt', 'r') #ファイルをオープン
fin2 = open('col2.txt', 'r')

for lines in zip(fin1, fin2):
    print '\t'.join(line.rstrip() for line in lines)

