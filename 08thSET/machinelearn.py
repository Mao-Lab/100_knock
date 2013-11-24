# -*- coding:utf-8 -*-

''' 第8セット内容:

	二格のデータを用いて、
	"前文脈の最後に出現する名詞句" と 
	"後文脈の最初に出現する動詞句" を
	素性として深層格の分類をする。

	*1:?がつく深層格は?を除いた値を正しいものとして扱う
	*2:深層格がx:不明が付されているものに関しては試験,
	   学習データから除外
'''

#=== Import modules
import sys
import os
from collections import Counter
import re, pprint

import cabochamod as cmod
from cabochamod import WordClass as wcls


# SML libraries
from sklearn.naive_bayes import BernoulliNB

#==============For Debugging===============
_debug = False

if _debug:
	print "####Running on debbugin mode####"

def dprint (str):
	if _debug:
		print "DEBUG:", str
#=========================================#

# global variable(Configuration)
path_data	= "./ngram_9/data/"			#元データ
vecTable = {}		#ベクタテーブル
testResults = [Counter() for idx in range(8)]
testResultKeys = ["R_Class", "F_NClass",
				  "F_Class", "R_NClass"]


# Defines Functions 
def calScore(counter):
 	dataNum = sum(counter.values())
	#正解率の計算
	accuracy = counter['R_Class'] + counter['R_NClass']
	accuracy = float(accuracy)/dataNum
	#精度(適合率)の計算
	precision = float(counter["R_Class"])/(counter["R_Class"] + counter["F_NClass"])
	#再現率の計算
	recall = float(counter["R_Class"])/(counter["R_Class"]+counter["F_Class"])
	#F値の計算
	Fmeasure = 0
	if recall + precision: 
		Fmeasure = 2.0 * recall * precision/(recall + precision)
	else:
		Fmeasure = -1

	return accuracy, precision, recall,Fmeasure

#Score
def score(clf, fname):
	testX, testy = gen_dataset(fname)
	
	results = [Counter() for idx in range(8)]
	for X, y in zip(testX, testy):
		ans = clf.predict(X)
		if y == ans : r, f = 1,0
		else : r, f = 0,1
		print "Detail: Predict=%d Ans=%d"% (y,ans)	
		
		for clsNum, counter in enumerate(results):
			if clsNum == y-1:
				counter["R_Class"] += r
				counter["F_Class"] += f
			else:
				counter["R_NClass"] += r
				counter["F_NClass"] += f
	
	sumCnt= Counter()

	for c in results:
		sumCnt += c
	print "TestData:%s\t%d\t" % (fname, sum(sumCnt.values())/8),
	print "%5.4f\t%5.4f\t%5.4f\t%5.4f" % calScore(sumCnt)
	
	global testResults
	for idx in range(8):
		testResults[idx] += results[idx]
#
def gen_vector_table(filelist):
	nounSet = set()
	verbSet = set()
	for fname in filelist:
		fin = open(fname)
		for line in fin:
			cols = line.strip().split("\t")
			if len(cols) < 3 : continue
			nounSet.add(cols[1].strip())
			verbSet.add(cols[2].strip())
			
	global vecTable
	for idx,word in enumerate(nounSet.union(verbSet)):
		vecTable[word] = idx
	
	return len(vecTable)

#Generate data set()
# X : vector 
# Y : vector values
def gen_dataset(fname):
	
	X = []
	y = []

	global vecTable
	veclen = len(vecTable)
	for line in open(fname):
		cols = line.strip().split("\t")

		if len(cols) < 3 : continue
		deep = cols[0]
		phrase1 = cols[1]
		phrase2 = cols[2]

		if "x" in deep: continue
		vecX = [0] * veclen
		vecX[vecTable[phrase1]] = 1
		vecX[vecTable[phrase2]] = 1

		X.append(vecX)
		y.append(int(deep.strip("?")))

	return X,y

#=== main ===
def main():
	global path_data
	#Get using file list
	fnls = [path_data+x for x in os.listdir(path_data)
						if os.path.isfile(path_data+x)]
	#Generate list for cross-validation
	# shapes = [validation file, [supervisors]]
	crs_ls = []
	for fname in fnls:
		crs_ls.append((fname,[x for x in fnls if x != fname]))
	
 	global testResults
	#Generate vector table
	gen_vector_table(fnls)
	#Supervisor Machine Learning
	for t, ls in crs_ls:
		clf = BernoulliNB()
		#Learning data
		for doc in ls:
			X,y = gen_dataset(doc)
			if doc == ls[0]: clf.fit(X,y)
			else: clf.partial_fit(X,y)
		#Scoring data
		score(clf, t)
	
	#Final Result
	#クラスごとのパラメータを見る
	cntall = Counter()
	print "##Each Class Results"
	for idx,cnter in enumerate(testResults):
		cntall += cnter
		print "Classification_Result(%d): %d/%d" % (idx+1, cnter["F_Class"]+cnter["R_Class"],sum(cnter.values())),
		print " %5.4f" * 4 % calScore(cnter)
	print
	print "##Meaning Result"
	print sum(cntall.values())
	print "All_Result: %d " % sum(cntall.values())/8,
	print " %5.4" * 4 % calScore(cntall)
	return

if __name__ == "__main__":
	main()
