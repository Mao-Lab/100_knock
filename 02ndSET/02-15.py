#! /usr/bin/python 
# -*- coding:utf-8 -*-

import re

tweetsCSV = 'tweets/tweets.csv'

regx = r'\@([0-9a-zA-Z_]*)[\s:]?'
linkFormat = '<a href="https://twitter.com/%s">@%s</a>'

def repl_id2taggedid(match_id_obj):
    usr_id = match_id_obj.group(1)
        return linkFormat % (user_id, user_id) 

def main():
    with open(tweetsCSV) as fin:
        fin.readline()
        for line in fin:
            cols = line.split(",")
            if len(cols) <  6 : continue
            tweet = cols[5]
            print re.sub(regx, repl_id2taggedid, tweet) 

if __name__ == '__main__':
    main()

