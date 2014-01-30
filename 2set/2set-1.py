#coding UTF-8

fr_tweet = open("col2.txt","r")

for line in fr_tweet.readlines():
	if "拡散希望" in line:
		print (line)

fr_tweet.close()