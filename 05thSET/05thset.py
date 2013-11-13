# -*- coding:utf-8 -*-

import sys
import fileinput
import types 
import mecabmod as MeCabMod
from mecabmod import WordClass as WClass
from optparse import OptionParser

#-------------main------------------------
if __name__ == "__main__":

	parser = OptionParser()
	parser.add_option("-v", "--verb",
			dest = "verb", default=False, action="store_true",
			help="extract verb morphemes")
	parser.add_option("-b", "--basic",
			dest = "basic", default=False, action="store_true",
			help="extract basic verb morphemes")
	parser.add_option("-n", "--noun",
			dest = "noun", default=False, action="store_true",
			help="extract nour morphemes")
	parser.add_option("-s", "--sahen",
			dest = "sahen", default=False, action="store_true",
			help="extract verb morphemes")
	parser.add_option("-c", "--chain",
			dest = "chain", default=False, action="store_true",
			help="extract verb morphemes")
	
	(opt, args) = parser.parse_args()

	str = sys.stdin.read()
	data = MeCabMod.analyze_morphemes(str)

	f = False
	for m in data:
		#動詞出力モードの場合
		if opt.verb and m.pos[0] == WClass.verb:
			if opt.basic:
				print m.base
			else:
				print m.surface
		elif opt.noun and m.pos[0] == WClass.noun:
			if 	opt.sahen:
				if m.pos[1].find("サ変") > -1:
					print m.surface
			else :
				print m.surface
		elif opt.chain:
			if m.pos[0] == WClass.noun:
				print m.surface,
				f = True
			elif f:
				print 
				f = False

