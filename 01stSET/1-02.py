# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname = argvs[1]

print "Step 2:Replace tab to space"
for line in open(fname):
    print line.replace("\t", " "),
print

"""
    解説:
    ファイルの容量が大きい場合を考え、イテレータを生成
    replaceを使って置換を行うだけ
"""
