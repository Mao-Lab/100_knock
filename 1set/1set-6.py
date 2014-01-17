# coding: UTF-8

#(6)
import sys

N = int(sys.argv[1])
f = open("address.txt")
data = f.read()
data = data.split("\n")
A = len(data)
for i in range(A-N,A):
	print (data[i].rstrip("\n"))
f.close()