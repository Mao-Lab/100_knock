# coding: utf-8
import sys

argvs = sys.argv

N = int(argvs[1])
temp = list()
with open('address.txt') as f:
    i = 0
    line = f.readline()
    while line:
        i = i + 1
        temp.append(line)
        line = f.readline()

    for j in range(i-N,i):
        print temp[j],
