# -*- coding: utf-8 -*-
#第3セット(30)(25)の出力を標準入力から読み込み、stemming.porter2を用いて語幹を最終列に追加し、mediline.txt.sent.tok.stemというファイルに保存せよ
from stemming.porter2 import stem
import sys
#1行1単語形式のテキストを作った movie_reviews.txt.tok
fin = open('movie_reviews.txt.sent.stem', 'r')

for line in fin:
    origin_word = line.rstrip()
    stem_word = stem(origin_word)
    print "%s\t%s" %(origin_word, stem_word)
