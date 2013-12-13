# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname, tailN = argv[1:2]

print "Step9:2列名-1列目をkeyとして降順にソート"
sortList = []
with open(fname) as fin:
    for line in fin:
        cols = line.strip().split("\t")
        if len(col) < 2 : continue
        ls.append(cols)

for line in sorted(key=lambda cols :(cols[2],　cols[1]), reverse=True):
    print l

"""
    解説:
    sorted関数を使う事でもsortされる。sorted関数はイテレータを返す。渡せるものはiteratableな変数。
    list型にはsortが実装されている。各要素からkeyを取り出す関数をわたしてやることで
    並び方を自由に指定してやることができる。
    ここでは、タプルを返してやることで2列目1列目の優先順位をつけることができる。
"""
