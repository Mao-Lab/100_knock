# !/usr/bin/env Python 	
# -*- coding:utf-8 -*- 

from collections import Counter

import re 


path = './movie_reviews.txt'

def main():
	wordCnt = Counter()
	with open(path) as fin:
		for line in fin:
			line = re.sub(r'\W+',' ',line.strip())
			words = line.strip().split(' ')
			for word in words:
				wordCnt[word] += 1

	for word, freq in wordCnt.most_common(100):
		print word, freq
 
if __name__ == '__main__':
	main()
