# coding: utf-8
import sys

def open_txt(file_name):
    f = open(file_name)
    line = f.readlines()
    f.close()
    return line

f1 = open_txt('col1.txt')

print f1[0]
print set(f1[0].encode)
