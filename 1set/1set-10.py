#coding UTF-8

fr_address = open("col2.txt","r")
words = fr_address.readlines()

 
from collections import Counter
word_freq = Counter(words)


for key, value in sorted(word_freq.items(), key=lambda x:x[1]):
	print (key)

fr_address.close()

