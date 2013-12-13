# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname = argv[1]

print "Step7:1列目の文字列の種類数を数える"
wordSet = set()
with open(fname) as fin:
    for line in fin:
        cols = line.strp().split("\t")
        wordSet.add(cols[0])              
print len(wordSet)

"""
    解説:
    setは重複を許さない集合のためのデータ構造。
    集合の演算。差集合、和集合などなど数々実装されている。
    内部は木構造になっているため、要素の探索が速い
    http://docs.python.jp/2.5/lib/types-set.html
"""
