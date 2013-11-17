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
import cabochamod as cmod
from cabochamod import WordClass as wcls

# SML libraries
from sklearn.naive_bayes import BernoulliNB

#==============For Debugging===============
_debug = True

if _debug:
	print "####Running on debbugin mode####"

def dprint (str):
	if _debug:
		print "DEBUG:", str
#=========================================#

# global variable(Configuration)
path_data	= "../Sample/work/"			#元データ
lat_prectx	= "../Sample/work/prectx/"	#解析済み前文脈
lat_pstctx	= "../Sample/work/postctx/"	#解析済み後文脈

#Extract feature from Chunk Class for SML
def extract_last_noun(chunk):
	print chunk
	return [m.pos for m in chunk 
			if m.pos == wcls.noun][-1]
def extract_first_verb(chunk):
	return [m.pos for m in chunk 
			if m.pos == wcls.verb][0]

#Generate data set()
# X : vector 
# Y : vector values
def gen_dataset(fname):
	path =  fname
	f = open(path)
	
	#形態素データの読み込み
	prectxes = cmod.read_laticedata(fname.replace(path_data,lat_prectx))
	pstctxes = cmod.read_laticedata(fname.replace(path_data,lat_pstctx))

	X = []
	Y = []
	f.readline() 	#1行目を飛ばす
	for idx, line in enumerate(f):
		cols = line.strip("").split("\t")
		if cols[0] == "x" : continue
		Y.append(int(cols[0].strip("?")))
		X.append([
			extract_last_noun(prectxes[idx]),
			extract_last_verb(pstctxes[idx])
			])
		print X[-1], Y[-1]
	f.close()
	f_prectx.close()
	f_pstctx.close()

	return X,Y

#=== main ===
def main():
	global path_data
	#Get using file list
	fnls = [path_data+x for x in os.listdir(path_data)
						if os.path.isfile(path_data+x)]

	#Generate list for cross-validation
	# shapes = [validation file, [supervisors]]
	crs_ls = []
	print fnls
	for fname in fnls:
		crs_ls.append((fname,[x for x in fnls if x != fname]))
	
	#Supervisor Machine Learning
	clf = BernoulliNB()
	for t, ls in crs_ls:
		for doc in ls:
			x, y = gen_dataset(doc)
			clf.partial_fit(x,y)
	return

if __name__ == "__main__":
		main()
