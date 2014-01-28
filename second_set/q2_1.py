# coding: utf-8
#第2セット(11)「拡散希望」という文字列で終わるツイートを抽出せよ
import sys

#自分のtwitterのつぶやきを１列に並べたものを利用
fin = open('mytweet.txt', 'r')

tl = list()
line = fin.readline()
while line:
    tl.append(line)
    line = fin.readline()

fin.close()

#「拡散希望」を含むツイートを抽出
for line in tl:
    if "拡散希望" in line:
        print line.strip()
