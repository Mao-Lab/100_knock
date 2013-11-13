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
import cabochamod as cmod


#==============For Debugging===============
_debug = True

if _debug:
	print "Running on debbugin mode"

def dprint (str):
	if __debug:
		print "DEBUG:", str
#=========================================#

# global variable(Configuration)
path_datai	= "../Sample/work/"			#元データ
lat_prectx	= "../Sample/work/prectx/"	#解析済み前文脈
lat_pstctx	= "../Sample/work/postctx/"	#解析済み後文脈



#=== main ===
def main():

	return

if __name__ = "__main__":
	main()
