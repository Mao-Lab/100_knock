# -*- coding:utf-8 -*-

##Mecab Module
VERSION = "0.0.1"

def read_laticedata(fname):
	f = open(fname)
	
	chunks = []
	str = ""
	#ファイルサイズが大きいときに備えて
	#文節ごとに読み込むようにする
	for line in f:
		str += line + "\n"
		if line.strip() == "EOS":
			chunks.extend(analyze_morphemes(str))
			str = ""
	f.close()
	return chunks

# 形態素解析開始
# TODO:分節ごとに読み込むように変更する
def analyze_morphemes(sentence):
	"""
	analyze_morphemsメソッド
	　引数１：sentence 文章
	　説明：
	　文章の形態素解析を行うメソッド．
	"""
	data = []
	chunks = []

	list = sentence.split("\n")

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
			chunks[-1].pos = chunks[-1]._get_phrase_pos()
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
		self.pos = ""
		self.independent_morph = None

	def _get_phrase_pos(self):
		#TODO:修飾関係からも句を推定する
		#自立である品詞から句の品詞を推定	
		POS1toMorph = dict[(m.pos1, m) for m in self.morphs]
		if "自立" in POS1toMorph:
			self.independent_morph = dict["自立"]
			return self.dependent_morph.pos
		else:
			if WordClass.noun in [m.pos for m in self.morphs]:
				return WordClass.noun
			else: return WordClass.adv

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
			if self.independent_morph.pos2 == "サ変"
				and idx > 0 
				and self.morphs[idx-1].pos1 == "サ変接続":
				return "".join([self.morphs[idx-1].base,
						  self.independent_morph.base])
			else : return self.independent_morph.base
		elif self.pos == WordClass.noun:
			return self.syzygy()

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
	pos2:品詞2
	base:原型（文字列）
	"""
	def __init__(self, str):
		list = str.strip("\n").split("\t")
		morphs = list[1].split(",")
		
		self.surface = list[0]
		self.pos = morphs[0]
		self.base = morphs[6]
		self.pos1 = morphs[1]
		self.pos2 = morphs[4]

	def tostring(self):
		str = " ".join([self.surface,self.pos,self.pos1,self.base])
		return str
#-----main



