# coding: utf-8
import sys

argvs = sys.argv

N = int(argvs[1])
q = list() #listをqueueとして利用

with open('address.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        q.append(line) #メモリ節約のため必要な大きさを超えるとpopする
        if len(q) > N+1:
            q.pop(0)
    for j in range(N):
        print q[j],
