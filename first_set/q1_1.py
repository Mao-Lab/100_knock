# coding: utf-8
import sys

argvs = sys.argv
fin = open(argvs[1])
line = fin.readline()

i=1
for line in fin:
    i = i + 1

fin.close()

print i,argvs[1]
