# -*- coding:utf-8 -*-

import fileinput
import math
import sys
import cabochamod as CaboChaMod
from cabochamod import WordClass as WClass
from collections import Counter


def genNounList(str):
	list = []
	sentences = CaboChaMod.analyze_morphemes(str)
	for chunks in sentences:
		for c in chunks:
			str = c.syzygy()
			if str != "" :
				list.append(str)
	return list

if __name__ == "__main__":
		

#CaboChaの解析データから連接名詞抽出 > *.nファイルとして保存
	nounList = []
	fileList = []

	for filename in sys.argv[1:]:
		f = open(filename)
		str = f.read()
		f.close()
		#形態素解析を行い、連接名詞を抽出
		ls = genNounList(str)
		nounList.extend(ls)
		dst = filename + '.n'
		f = open(dst,"w")
		f.write("\n".join(ls))
		f.close()
		print "Create:" + dst
		fileList.append(dst)


#名詞リストをuniqする
	nounList = list(set(nounList))

#名詞データからTF*IDF値の算出 > tfidf.txtに出力
	print "Calculate TF*IDF: File Num %d" % (len(fileList))  
	cntList = []
	d = Counter()
	for name in fileList:
		f = open(name)
		str = f.read()
		f.close()
		#各ファイルの名詞句の出現頻度数え上げ
		cnt = Counter(str.split("\n"))
		cntList.append(cnt)
	str = ""
	for n in nounList:
		w = 0
		df = 0
		for c in cntList:
			w += c[n]
			if c[n] > 0:
				df += 1
		idf = math.log(len(fileList)/df)
		str +=  "%s\t%f\t%d\t%f\n" % (n, w*idf, w, idf)

	f = open("tfidf.txt","w")
	f.write(str)
	f.close()



