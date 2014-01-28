  #! /usr/bin/python 
# -*- coding:utf-8 -*-

import re

tweetsCSV = 'tweets/tweets.csv'

def main():
	with open(tweetsCSV) as fin:
		fin.readline()

		for line in fin:
			cols = line.split(",")
			if len(cols) <  6 : continue
			tweet = cols[5]

			r = re.compile("\@[0-9a-zA-Z_]*[\s:]?")
			users = r.findall(tweet)
			if len(users) > 0:
				print users

if __name__ == '__main__':
	main()
 
