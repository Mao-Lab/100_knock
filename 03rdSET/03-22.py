# !/usr/bin/env Python	
# -*- coding:utf-8 -*- 

import re

path = './movie_reviews.txt'

def main():
    with open(path) as fin:
        for line in fin:
            print re.sub( r"\s\.([A-Z])", r' .\n\1', line.strip())


if __name__ == '__main__':
    main()
