#-*- coding : uft-8 -*-

import os.path
import fileinput
import marshal

dic = {}
dicPath = "./Dictionary"
srcPath ="../Sample/inflection.table.txt" 

def createDic():
	f = open(srcPath,"r")
	lines = f.readlines()
	f.close()

	for l in lines:
		data = l.split("|")
		if len(data) > 6:
			list = [data[1], data[3], data[6]]
			dic[data[0]] = list
	f = open(dicPath,"wb")
	marshal.dump(f)
	f.close()

def loadDic():
	global dic
	f = open(dicPath,"rb")
	dic = marshal.load(f)
	f.close()

def lookupWord(word, flag = False):
	global dic
	w = word.strip()
	try:
		data = dic[w]
		return data
	except KeyError:
		if flag:
			return ""
		else:
			return lookupWord(w.lower(),True)

def InputCheck():
	global dic
	while True:
		ri = raw_input("Please words(To quit:\"q\"):")
		if (ri == "q"):
			return
		data = lookupWord(ri)
		if data == "":
			print "Not found in Dictinoary"
		else:
			print data


# ---- main-------

if not os.path.exists(dicPath):
	createDic()
loadDic()

# Step 39
#print "Lookup word in Dictionary"
#for l in inputs:
#	print l.strip(), lookupWord(l)

# Step 40
#print "Display only words not found in Dictionary"
#for l in fileinput.input():
#	w = l.strip()
#	data = lookupWord(w)
#	if data == "":
#		print w

# Step 41
print "Step 42:Display the words found more than 3 times in Dictionary"
cnt = {}
for l in fileinput.input():
	w = l.strip()
	data = lookupWord(w)
	if not data == "":
		if w in cnt:
			cnt[w] = cnt[w] + 1
		else:
			cnt[w] = 1
for k,v in cnt.items():
	if v >= 3:
		print k,v



