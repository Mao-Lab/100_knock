# coding: utf-8
#第2セット(13)非公式RTのツイートの中で、RT先へのコメント部分のみを抽出せよ
import sys

#自分のtwitterのつぶやきを１列に並べたものを利用
fin = open('mytweet.txt', 'r')

tl = list()
line = fin.readline()
while line:
    tl.append(line)
    line = fin.readline()

fin.close()

#非公式RTかどうかを判断、非公式RTにはRTの前にコメントが含まれると仮定
for x in range(len(tl)):
    tl[x] = tl[x].rstrip()
    if(tl[x].startswith('RT') and not tl[x].split('RT')[0]):
        print tl[x].split('RT')[1]

