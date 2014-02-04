 # !/usr/bin/env Python 	
# -*- coding:utf-8 -*- 

import re

path = './movie_reviews.txt'

def main():
	with open(path) as fin:
		for line in fin:
			line = re.sub(r'\W+',' ',line.strip())
			words = line.strip().split(' ')
			for word in words:
				print word, word.lower()
			print


if __name__ == '__main__':
	main()
