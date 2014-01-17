# coding: UTF-8

#(5)
import sys

N = int(sys.argv[1])
f = open("address.txt")

for i in range(N):
	print (f.readline().rstrip("\n"))
f.close()