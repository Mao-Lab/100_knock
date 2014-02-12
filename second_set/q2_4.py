# coding: utf-8
#第2セット(14)ツイッターのユーザ名(@で始まる文字列)を抽出せよ
import sys
import re
#自分のtwitterのつぶやきを１列に並べたものを利用
fin = open('mytweet.txt', 'r')

tl = list()
line = fin.readline()
while line:
    tl.append(line.rstrip('\n'))
    line = fin.readline()

fin.close()

#RTを取り除いてから@から始まるユーザ名を取り出す
for x in range(len(tl)):
    tl[x] = tl[x].lstrip('RT ')
    if('@' in tl[x]):
        print tl[x].rsplit(' ')[0].rstrip(':')
