# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname, tailN = argv[1:2]

print "Step8:2列名をkeyとして昇順にソート"
sortList = []
with open(fname) as fin:
    for line in fin:
        cols = line.strip().split("\t")
        if len(col) < 2 : continue
        ls.append(cols)
sortList.sort(key=lambda cols: cols[1])
for line in sortList : print line

"""
    解説:
    list型にはsortが実装されている。各要素からkeyを取り出す関数をわたしてやることで
    並び方を自由に指定してやることができる。
"""
