# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname, tailN = argv[1:2]

print "Step6:最後" + argvs[2] + "行だけ表示"
tailN = int(argvs[2])
from collections import deque
with open(filename) as fin:
    for line in deque(f, maxlen=tailN):
        print line 

"""
    解説:
    ファイルが大きくなると、メモリの関係から読み込めない場合がでてくる。
    愚直に実装すれば、ファイルの行数を数える→イテレータである行数以降のみ出力する　といったような
    処理が考えられるが、処理が助長だし汚い。
    今回はdequeの仕組みを利用して、tailを行う。
    dequeは、後ろからも前からもappend,popがO(1)が行えるデータ構造。
    宣言時にmaxlenを指定してやることで、配列の大きさを一定に保ってやることができる。    
    itertoolsのdropwhileを使っても良いと思う。
    参照:http://ja.pymotw.com/2/itertools/
"""
