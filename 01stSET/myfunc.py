# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname = argvs[1]

print "Step 1:Count File lines"
print sum([1 in open(filename)])

print "Step 2:Replace tab to space"
for line in open(fname):
    print line.replace("\t", " "),
print

print "Step 3:Cut line1 and line2"
with foutCol1 
foutCol1 = open("col1.txt", "w+")
foutCol2 = open("col2.txt", "w+")

for line in open(filename):
	cols = line.strip().split("\t")
	if len(col) < 2: continue
 	col1.write(col[0] + "\n")
    col2.write(col[1] + "\n")

col1.close()
col2.close()

fname1, fname2, fname3 = argvs[1:3]
 print "Step4:Combine col1.txt and col2.txt"
with open(fname1) as fin1, open(fname2) as fin2,
    open(fname3,"w+") as fout:
    for col1, col2 in zip(fin1, fin2):
        fout.write("\t".join(col1, col2))
print "Step5:先頭" + argvs[2] + "行だけ表示"
headN = int(argvs[2])
from itertools import islice
with open(filename) as fin:
    for line in islice(fin, headN):
        print line

print "Step6:最後" + argvs[2] + "行だけ表示"
tailN = int(argvs[2])
from collections import deque
with open(filename) as fin:
    for line in deque(f,maxlen=tailN)
        print line 

print "Step7:1列目の文字列の種類数を数える"
wordSet = set()
with open(filename) as fin:
    for line in fin:
        cols = line.strp().split("\t")
        wordSet.add(cols[0])              
print len(wordSet)

print "Step8:2列名をkeyとして昇順にソート"
sortList = []
with open(filename) as fin:
    for line in fin:
        cols = line.strip().split("\t")
        if len(col) < 2 : continue
        ls.append(cols)
sortList.sort(key=lambda cols: cols[1])
for line in sortList : print line

print "Step9:2列名-1列目をkeyとして降順にソート"
for line in sorted(key=lambda cols:(cols[2],cols[1]), reverse=True):
    print l

print "Step10:1カラム目の出現頻度を調べ、出現頻度の高い順に並び替え入力にはcol1.txtを用いる"
from collections import Counter
wordCnt = Counter()
with open(filename) as fin:
    for line in fin:
        cols = line.strp().split("\t")
        wordCnt[cols[0]]             
for k, v in sorted(wordCnt.items(), key=lambda cols:cols[1], reverse=True):
    print k, v 