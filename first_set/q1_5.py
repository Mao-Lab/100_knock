# coding: utf-8
import sys

argvs = sys.argv
N = int(argvs[1]) #Nに自然数Nを引数としてint型に変換し代入
with open('address.txt') as f: #address.txtをfとして開く
    for i in range(N):
        print f.readline(),
