#! /usr/bin/python 
# -*- coding:utf-8 -*-

tweetsCSV = 'tweets/tweets.csv'

def main():
    with open(tweetsCSV) as fin:
        fin.readline() 
        for line in fin:
            cols = line.split(",")
            if len(cols) <  6 : continue
            if("拡散希望" in cols[5]): 
                print(cols[5]) 


if __name__ == '__main__':
    main()

