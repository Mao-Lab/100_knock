# coding: utf-8
#第2セット(15)ツイッターのユーザ名を、そのユーザーのページヘリンク(<a href="https://twitter.com/#!/xxxxx">@xxxxx</a>で囲まれたHTML断片）に置換せよ
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

#@を取り除き、URLを追加
for x in range(len(tl)):
    tl[x] = tl[x].lstrip('RT ')
    if('@' in tl[x]):
        tl[x] = tl[x].rsplit(' ')[0].rstrip(':')
        tl[x] = 'https://twitter.com/' + tl[x].strip('@')
        print tl[x]
