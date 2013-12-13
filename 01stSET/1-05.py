# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname, headN = argv[1:2]
print "Step5:先頭" + headN + "行だけ表示"

from itertools import islice
with open(filename) as fin:
    for line in islice(fin, headN):
        print line

"""
    解説:
    itertoolsnのisliceを使うことで省メモリかつ早いやつが書けるらしい
    このスライサを利用してheadするだけ
    参照:http://ja.pymotw.com/2/itertools/

"""
