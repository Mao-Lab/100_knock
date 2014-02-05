#! /usr/bin/python 
# -*- coding:utf-8 -*-

import re

tweetsCSV = 'tweets/tweets.csv'

regx =  u'([一-龠]+)\(([A-Z]+)\)'

def main():
    with open(tweetsCSV) as fin:
        fin.readline() 
        for line in fin:
            cols = line.split(",")
            if len(cols) <  6 : continue
            tweet = cols[5] 
            matches = re.finditer(regx, tweet.decode('utf-8'))
            for matchobj in matches:
                print  matchobj.group(1).encode('utf-8'), matchobj.group(2).encode('utf-8')


if __name__ == '__main__':
    main()

