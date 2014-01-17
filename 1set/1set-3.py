# coding: UTF-8

#(3)
f = open("address.txt")
data1 = open("col1.txt","w")
data2 = open("col2.txt","w")

for line in f.readlines():
	line = line.split("\t")
	data1.write(line[0]+"\n")
	data2.write(line[1])

f.close()
data1.close()
data2.close()