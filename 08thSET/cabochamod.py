# -*- coding:utf-8 -*-

## import files
import mecabmod as mmod
from mecabmod import WordClass

##CaboCha Module
VERSION = "0.0.1"

class Chunk:
	"""
	文節クラス
	morphs:形態素クラスのリスト
	dst:係り先文節インデックス番号
	srcs:係り元文節インデックス番号のリスト
	"""
	def __init__(self, str):
		array = str.strip().split(" ")
		self.morphs = []
		self.dst = int(array[2].strip("D"))
		self.srcs = []
		self.pos = ""
		self.independent_morph = None

	def _get_phrase_pos(self):
		#TODO:修飾関係からも句を推定する
		#自立である品詞から句の品詞を推定
		POS1toMorph = dict([(m.pos1, m) for m in self.morphs])
		if "自立" in POS1toMorph:
			self.independent_morph = POS1toMorph["自立"]
			return self.independent_morph.pos
		else:
			POS2Morph = dict([(m.pos, m) for m in self.morphs])
			if WordClass.noun in POS2Morph:
				self.independent_morph = POS2Morph[WordClass.noun]
				return WordClass.noun
			elif WordClass.adv in POS2Morph:
				self.independent_morph = POS2Morph[WordClass.adv]
				return WordClass.adv
			else :
				self.independent_morph = self.morphs[-1]
				return self.independent_morph.pos
		 
	def tostring(self):
		string = "%s:%d %s:%s\n%s" % (
				"係先Index", self.dst,
				"係元文節Index",",".join(map(lambda x: str(x), self.srcs))
				,"\n".join(map(lambda x: x.tostring(),self.morphs))
				)
		return string
	
	def phrase(self):
		if self.pos == WordClass.verb:
			idx = [m.pos1 for m in self.morphs].index("自立")
			if self.independent_morph.pos2 == "サ変・スル" and idx > 0 and self.morphs[idx-1].pos1 == "サ変接続":
				return "".join([self.morphs[idx-1].base,
						  self.independent_morph.base])
			else :return self.independent_morph.base
		elif self.pos == WordClass.noun:
			return self.syzygy()
		else : return self.independent_morph.base

	def hasPOS(self,wc):
		for m in self.morphs:
			if m.pos == wc:
				return True
		return False

	def syzygy(self):
		str = ""
		for m in self.morphs:
			if m.pos == WordClass.noun:
				str += m.surface
		return str



