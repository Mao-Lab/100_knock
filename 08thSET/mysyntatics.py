# -*- coding:utf-8 -*-

## import files
import cabochamod as cmod

import fileinput
from collections import deque

def read_latticeFile(path):
	sentences = []
	for line in open(path):
		readline_lattice(sentences, line)
	return sentences

def read_lattice(paragraph=None):
	sentences = []
	lines = []
	if paragraph is None:
		lines = fileinput.input()
	else: 
		lines = paragraph.split("\n")
	
	for line in lines:
		readline_lattice(sentences,line)
	return sentences

def readline_lattice(sentences, lattice_line):
	line = lattice_line.strip()
	
	#空の場合は例外を投げる
	if not line: raise LatticeFormatErrorException(line)

	if not sentences : sentences.append([])
	chunks = sentences[-1]
	
	if line == "EOS":
		#係り受け元のリストを更新する
		for i,c in enumerate(chunks):
			c.pos = c._get_phrase_pos()
			if c.dst > -1:
				chunks[c.dst].srcs.append(i)
		sentences.append([])		#空のchunkリストを追加		
	elif line[0] == "*" and line.find("記号") < 0:
		chunks.append(cmod.Chunk(line))
	else:
		print chunks
		chunk = chunks[-1]
		chunk.morphs.append(cmod.mmod.Morph(line))
	

class LatticeFormatErrorException(Exception):
	def __init__(self, lattice):
		self.lattice = lattice
	def __str__(self):
		return "Lattice Format Error:[%s] is wrong format" % self.lattice

def main():
	sentences = []

if __name__ == "__main__":
	main()


