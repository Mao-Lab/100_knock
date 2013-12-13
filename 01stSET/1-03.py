# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname1, fname2, fname3 = argvs[1:3]

print "Step 3:Cut line1 and line2"
with open(fname1, "w+") as foutCol1, open(fname2, "w+") as foutCol2,
    open(fname3) as fin:
    if len(col) < 2:
        continue
    col1.write(col[0] + "\n")
    col2.write(col[1] + "\n")

"""
    解説:
    ファイルの容量が大きい場合を考え、イテレータを生成
    ファイルを開く時はwithステートメントを利用するとiwithから出た時に自動的にcloseされる。
    スコープが明示的に決まるので使うと良いと思われる。

"""
