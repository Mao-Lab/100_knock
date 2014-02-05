#! /usr/bin/python      
# -*- coding:utf-8 -*-  

tweetsCSV = 'tweets/tweets.csv'

def main():
    with open(tweetsCSV) as fin:
        fin.readline() 
        for line in fin:
            cols = line.split(",")
            if len(cols) <  6 : continue
            if cols[5].endswith("なう") :
                    print cols[5]


if __name__ == '__main__':
    main()
