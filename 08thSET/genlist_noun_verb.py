# -*- coding:utf-8 -*-

import mysyntatics as syntcsMod

#Extract feature from Chunk Class for SML
def extract_last_noun(chunks):
	return [ c for c in chunks
			if c.pos == wcls.noun][-1].phrase()
def extract_first_verb(chunk):
	return [ c for c in chunks 
			if c.pos == wcls.verb][0].phrase()

# main function
def main():
	sentences = syntcsMod.read_lattice()
	for chunks in sentences:
		for chunk in chunks:
			print chunk.pos, chunk.phrase()
			print chunk.tostring() 
			print 
	return

if __name__ == "__main__":
	main()


