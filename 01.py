# config: UTF-8

#1set (1)
f = open('address.txt')
data = f.read()
f.close()

print data.count('\n')
