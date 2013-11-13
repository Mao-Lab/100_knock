# -*- coding:utf-8 -*-

##Mecab Module
VERSION = "0.0.1"


# 形態素解析開始
def analyze_morphemes(sentences):
	"""
	analyze_morphemsメソッド
	　引数１：sentence 文章
	　説明：
	　文章の形態素解析を行うメソッド．
	"""
	data = []
	chunks = []

	list = sentences.split("\n")

	for l in list:
		l = l.strip()
		if l == "": continue
		if l == "EOS":
			#係り受け元のリストを更新する
			for i,c in enumerate(chunks):
				if c.dst > -1:
					chunks[c.dst].srcs.append(i)
			data.append(chunks)
			chunks = []
		elif l[0] == "*":
			chunks.append(Chunk(l))
		else:
			m = Morph(l)
			chunks[-1].morphs.append(m)
	
	return data

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

	def tostring(self):
		string = "%s:%d %s:%s\n%s" % (
				"係先Index", self.dst,
				"係元文節Index",",".join(map(lambda x: str(x), self.srcs))
				,"\n".join(map(lambda x: x.tostring(),self.morphs))
				)

		return string
	
	def phrase(self):
		
		return "".join(
			map(lambda x:x.surface,
			filter(lambda x:x.pos1 !="非自立",self.morphs)))

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


#形態素モジュール
class Morph:
	"""
	形態素クラス
	surface:表層（文字列）
	pos:品詞（配列にて格納）
	pos1:品詞1
	base:原型（文字列）
	"""
	def __init__(self, str):
		list = str.strip("\n").split("\t")
		morphs = list[1].split(",")
		
		self.surface = list[0]
		self.pos = morphs[0]
		self.base = morphs[6]
		self.pos1 = morphs[1]
	def tostring(self):
		str = " ".join([self.surface,self.pos,self.pos1,self.base])
		return str
#-----main



