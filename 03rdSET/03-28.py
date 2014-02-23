# !/usr/bin/env Python
# -*- coding:utf-8 -*-

from collections import Counter

import re


path = './movie_reviews.txt'


def ngrams(src, n):
    for idx in xrange(len(src) - n):
        yield src[idx:idx + n]


def main():
    ngramCnt = Counter()
    with open(path) as fin:
        for line in fin:
            line = re.sub(r'\W+', ' ', line.strip())
            words = line.strip().split(' ')
            for word in words:
                for ngram in ngrams(word, 2):
                    ngramCnt[ngram] += 1

    for ngram, freq in ngramCnt.most_common(100):
        print ngram, freq

if __name__ == '__main__':
    main()
