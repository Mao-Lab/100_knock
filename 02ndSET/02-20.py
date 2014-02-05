#! /usr/bin/python 
# -*- coding:utf-8 -*-

import re

tweetsCSV = 'tweets/tweets.csv'

regx =  u'([^一-龠 ァ-ヴぁ-ん"]*\([^一-龠0-9ァ-ヴ]{2,10}\)[^一-龠 ァ-ヴぁ-ん"]*)'

def extract_regx(text,r):
    matches = re.finditer(regx, text.decode('utf-8'))
    for matchobj in matches:
        for pattern in matchobj.groups():
            if pattern is None: continue
            print pattern.encode('utf-8')	


def main():
    with open(tweetsCSV) as fin:
        fin.readline() 
        for line in fin:
            cols = line.split(",")
            if len(cols) <  6 : continue
            tweet = cols[5]
            extract_regx(tweet, regx)


if __name__ == '__main__':
    main()


