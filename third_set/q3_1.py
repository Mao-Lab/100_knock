# -*- coding: utf-8 -*-
#第3セット(21)標準入力から英語のテキストを読み込み、ピリオドを文の区切りとみなし一行一文の形式で標準出力に書き戻せ
import sys

fin = open('movie_reviews.txt', 'r')

#ファイルを一行ずつ読み込み
for fline in fin:
    #改行コードを削除
    fline = fline.rstrip('\n')
    #英語の単語ごとにリストに分割
    fline = fline.split(' ')
    #単語ごとに走査
    for line in fline:
        #'.'で改行する
        if '.' in line:
            print line
        else:
            print line,
fin.close()

#結果の確認
#grep -c "\."で"."の数を確認32162
#wc -lで行数を確認32163 最後のコンマの後の改行1行が余分にたされる
