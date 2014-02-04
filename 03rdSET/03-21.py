# !/usr/bin/env Python 	
# -*- coding:utf-8 -*- 

path = './movie_reviews.txt'

def main():
	with open(path) as fin:
		for line in fin:
			print line.strip().replace(" .", ".\n")

if __name__ == '__main__':
	main()
