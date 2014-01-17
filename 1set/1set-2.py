# coding: UTF-8

#(2)
print ("(2)")
f = open("address.txt")
data = f.read()

Answer1 = data.replace('\t',' ')
print (Answer1)