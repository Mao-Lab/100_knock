# coding: utf-8
import sys

argvs = sys.argv
f = open(argvs[1])
line = f.readline()

i=0
while line:
    i = i + 1
    line = f.readline()
f.close

print i,argvs[1]
