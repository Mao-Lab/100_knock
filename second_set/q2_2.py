# coding: utf-8
#第2セット(12)「なう」という文字列で終わるツイートを抽出せよ
import sys

#自分のtwitterのつぶやきを１列に並べたものを利用
fin = open('mytweet.txt', 'r')

tl = list()
line = fin.readline()
while line:
    tl.append(line)
    line = fin.readline()

fin.close()

#「なう」で終わるツイートを抽出
for x in range(len(tl)):
    tl[x] = tl[x].rstrip()
    if(tl[x].endswith("なう")):
        print tl[x]
