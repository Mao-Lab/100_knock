# -*- coding:utf-8 -*-

import sys
import MeCab
import types 


##Mecab Module 
VERSION = "0.0.1"

mecab = MeCab.Tagger('-Ochasen')

# 形態素解析開始
def analyze_morphemes(sentence):
	"""
	analyze_morphemsメソッド
	　引数１：sentence 文章
	　説明：
	　文章の形態素解析を行うメソッド．
	"""
	global mecab
	morphs = []
	node = mecab.parseToNode(sentence)
	node = node.next
	while node:
		if str(node.surface) == "EOS":
			break
		else:
			morphs.insert(len(morphs), Core(node))
		node = node.next
	return morphs


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

#形態素モジュール
class Core:
	"""
	形態素クラス
	surface:表層（文字列）
	pos:品詞（配列にて格納）
	conjForm:活用形（文字列）
	conjType:体系（文字列）
	base:原型（文字列）
	"""
	def __init__(self,node):
		self.pos = []
		self.surface = node.surface
		array = node.feature.split(",")
		for i in range(4):
			self.pos.insert(i, array[i])
		self.conjForm = array[4]
		self.base = array[6]
		if len(array) > 7:
			self.read = array[7]
			self.pron = array[8]

