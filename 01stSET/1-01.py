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

"""
    解説:
    ファイルの容量が大きい場合を考え、イテレータを生成
    リスト内包表記によって、行数だけの数の中身が1の配列を生成し総和を出力＝ファイル行数
    D
"""
