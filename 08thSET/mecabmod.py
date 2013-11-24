# -*- coding:utf-8 -*-

#品詞の種類クラス
class WordClass:
	noun = "名詞"
	verb ="動詞"
	adj = "形容詞"
	adjnoun="形容動詞"
	adv="副詞"
	pp="助詞" 
	aux="助動詞" 
	inj="感動詞"
	conj="接続詞"
	sign="記号"
 
#形態素クラスi
class Morph:
	"""
	形態素クラス
	surface:表層（文字列）
	pos:品詞（配列にて格納）
	pos1:品詞1
	pos2:品詞2
	base:原型（文字列）
	"""
	def __init__(self, str):
		ls = str.strip("\n").split("\t")
		if len(ls) < 3 :
			ls.insert(0, " ")
		morphs = ls[1].split(",")
	
		self.surface = ls[0]
		self.pos = morphs[0]
		self.base = morphs[6]
		self.pos1 = morphs[1]
		self.pos2 = morphs[4]

	def tostring(self):
		str = " ".join([self.surface,self.pos,self.pos1,self.base])
		return str
