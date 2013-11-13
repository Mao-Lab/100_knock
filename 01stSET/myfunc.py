# -*- coding:UTF-8 -*-


import sys
import codecs

argvs = sys.argv
argc = len(argvs)

print argvs
print argc
print 

if(argc < 2):
		print "Usage: #python %s filename" % argvs[0]
		quit()

f = open(argvs[1])

print "Step 1:Count File lines"
lines = f.readlines();
f.close()
print len(lines)
print

print "Step 2:Replace tab to space"
for l in lines:
		print l.replace("\t"," "),
print

print "Step 3:Cut line1 and line2"
col1 = open("col1.txt","w+")
col2 = open("col2.txt","w+")
for l in lines:
		col = l[:-1].split("\t")
		if(len(col) > 1 ):
			col1.write(col[0]+"\n")
			col2.write(col[1]+"\n"),
print
col1.close()
col2.close()


print "Step4:Combine col1.txt and col2.txt"
col1 = open("col1.txt","r")
col2 = open("col2.txt","r")
col  = open("col.txt","w+")

lines = col1.readlines()
for l in lines:
		col.write("\t".join([l[:-1],col2.readline()])),
print

print "Step5:先頭"+argvs[2]+"行だけ表示"
f = open(argvs[1])
lines = f.readlines()
f.close()

N = len(lines)
n = int(argvs[2])
for l in range(0,min(n,N)):
		print lines[l].strip()
print

print "Step6:最後"+argvs[2]+"行だけ表示"
for l in range(max(N-n,0),N):
		print lines[l].strip()
print
 
print "Step7:1列目の文字列の種類数を数える" 
cnt = {}
for l in lines:
		col = l.strip().split("\t")
		if col[0] in cnt: 
				cnt[col[0]] += 1
		elif col[0] != "":
				cnt[col[0]] = 1
print len(cnt)

print "Step8:2列名をkeyとして昇順にソート"
#リストの作成を行う
ls = []
for l in lines:
		col = l[:-1].split("\t")
		if len(col) > 1:
			ls.append(col)
print
ls.sort(key=lambda ls:ls[1])
for l in ls:
		print l  
print

print "Step9:2列名-1列目をkeyとして降順にソート"
ls.sort(key=lambda ls:ls[0], reverse=True)
ls.sort(key=lambda ls:ls[1], reverse=False)
#key = itemgetter(1,2)でも可能か？
for l in ls:
		print l
print

print "Step10:1カラム目の出現頻度を調べ、出現頻度の高い順に並び替え、入力にはcol1.txtを用いる"
#cntをそのまま用いてソート
for k,v in sorted(cnt.items(), key=lambda x:x[1], reverse=True):
		print k,v
print

