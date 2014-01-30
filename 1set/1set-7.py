#coding UTF-8

fr_col1 = open("col1.txt","r")
set_col1 = set()

for line in fr_col1:
	set_col1.add(line)
fr_col1.close()
print (len(set_col1))
