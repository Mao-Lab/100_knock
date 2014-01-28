 #! /usr/bin/python 
# -*- coding:utf-8 -*-

tweetsCSV = 'tweets/tweets.csv'

def main():
	with open(tweetsCSV) as fin:
		fin.readline()

		for line in fin:
			cols = line.split(",")
			if len(cols) <  6 : continue
			
			tweets = cols[5].strip("\"").split("RT @")

			if len(tweets) < 2 or len(tweets[0]) < 2 :
				continue
			print tweets[0]


if __name__ == '__main__':
	main()
 
