# coding: UTF-8

#(4)
f1 = open("col1.txt","r")
f2 = open("col2.txt","r")
out = open("(4).txt","w")
data1 = f1.read()
data2 = f2.read()
data1 = data1.split("\n")
data2 = data2.split("\n")

for line in zip(data1,data2):
	out.write("\t".join(line)+"\n")
out.close()
f1.close()
f2.close()