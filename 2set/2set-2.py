#  coding: utf-8 

fr_tweet = open("tweets.txt", "r")

for line in fr_tweet:
	line = line.rstrip()
	if line.endswith("なう"):
		print (line)

fr_tweet.close()