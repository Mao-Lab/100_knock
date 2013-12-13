# -*- coding:UTF-8 -*-

import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()

fname = argv[1:2]

print "Step10:1カラム目の出現頻度を調べ、出現頻度の高い順に並び替え入力にはcol1.txtを用いる"
from collections import Counter
wordCnt = Counter()
with open(fname) as fin:
    for line in fin:
        cols = line.strp().split("\t")
        wordCnt[cols[0]]             
for k, v in sorted(wordCnt.items(), key=lambda cols: cols[1], reverse=True):
    print k, v 

"""
    解説:
    リッチなデータ構造としてCollectionsにdefaultDic, Counter等がある。
    defaultDicはインデクサで要素にない物がアクセスされた場合に初期値を勝手に与えてくれる。
    つまりif文とか使わなくてもいい。
    CounterはdefaultDicで初期値を全て0にしもの。set型で数が数えれるようになったみたいなもの
    出現頻度などの数を数えるならば、Counterを使用した方が良いと思われる。
"""
