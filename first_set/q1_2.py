# coding: utf-8
import sys

argvs = sys.argv
f = open(argvs[1])

line = f.readline()

while line:
    print line.replace('\t', ' '),
    line = f.readline()
f.close
