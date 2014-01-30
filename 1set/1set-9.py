#coding UTF-8

fr_address = open("address.txt","r")
 
list_address=[]

for line in fr_address.readlines():
	list_address.append(line.split("\t"))

print (list_address)
fr_address.close()

for key, value in sorted(list_address, key=lambda x:(x[1], x[0]), eversed=True):
	print (key, value)