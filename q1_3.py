# coding: utf-8
import sys

argvs = sys.argv


f  = open(argvs[1])
f1 = open('col1,txt','w')
f2 = open('col2.txt','w')

line = f.readline()
col1 = []
col2 = []
i=0
while line:
    col1.append(line.split('\t')[0])
    col2.append(line.split('\t')[1])
    f1.writelines(col1[i]+"\n")
    f2.writelines(col2[i])
    i=i+1
    line = f.readline()

f.close
f1.close
f2.close

