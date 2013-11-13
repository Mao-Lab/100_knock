# -*- coding:utf-8 -*-
import sys
import fileinput
import cabochamod as CaboChaMod
from cabochamod import WordClass as WClass
from collections import Counter


tfidfPath = "tfidf_top100.txt"

def magVec(v):
 	return sum([x**2 for x in v.values()])**0.5 

def cosSim(v1 ,v2):
	#keyの和集合リストを作る
	keys = list(set(v1.keys() +  v2.keys()))
	mag12 = magVec(v1)*magVec(v2)
	s = sum([v1[k]*v2[k] for k in keys])
	return s / mag12

#高TF*IDF値のワードの取得
words = []
vecCtx = {} #文脈ベクトル
for l in fileinput.input(tfidfPath):
	w = l.split("\t")[0]
	words.append(w)
	vecCtx[w] = Counter()
	
fileList = sys.argv[1:]
flt = lambda x: x.pos == WClass.noun \
		or x.pos == WClass.verb \
		or x.pos == WClass.adj

for fname in fileList:
	f = open(fname)
	str = f.read()
	f.close()
	sentences = CaboChaMod.analyze_morphemes(str)
	for chunks in sentences:
		for c in chunks:
			#文脈の出力
			if c.syzygy() in words:
				#係り先の単語の出力
				for m in filter(flt,chunks[c.dst].morphs):
					vecCtx[c.syzygy()]["->"+m.base] += 1
				#係も元の単語の出力
				for ms in map(lambda i:chunks[i].morphs, c.srcs):
					for m in filter(flt, ms):
						vecCtx[c.syzygy()]["<-"+m.base] += 1
#文脈ベクトルの一覧表示
for k,v in vecCtx.items():
	print "%s\t"% (k),
	#文脈ベクトルの計算
	mag = magVec(v)
	for str,cnt in v.items():
		print "%s:%f" % (str, cnt/mag),
	print
print "文脈ベクトルのコサイン類似度の計算"
#文脈ベクトルのコサイン類似度の計算
ls = [[[k1,v1],[k2,v2]]	for k1,v1 in vecCtx.items()
						for k2,v2 in vecCtx.items()]
for v in ls:
	if v[0][0] == v[1][0] : continue
	sim = cosSim(v[0][1],v[1][1])
	if sim > 0.6:
		print "%f\t%s\t%s" % (sim, v[0][0], v[1][0])



