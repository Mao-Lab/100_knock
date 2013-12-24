# coding: utf-8
import sys

argvs = sys.argv

fin  = open(argvs[1])
fin1 = open('col1.txt','w')
fin2 = open('col2.txt','w')

line = fin.readline()
while line:
    fin1.writelines(line.split('\t')[0]+'\n')
    fin2.writelines(line.split('\t')[1])
    line = fin.readline()

fin.close()
fin1.close()
fin2.close()

