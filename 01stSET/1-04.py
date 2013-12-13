# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname1, fname2, fname3 = argvs[1:3]

print "Step4:Combine col1.txt and col2.txt"
with open(fname1) as fin1, open(fname2) as fin2,
    open(fname3,"w+") as fout:
    for col1, col2 in zip(fin1, fin2):
        fout.write("\t".join(col1, col2))

"""
    解説:
    ファイルの容量が大きい場合を考え、イテレータを生成
    zipで1つにまとめファイルに書き込みを行う。

"""
