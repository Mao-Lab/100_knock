# -*- coding:UTF-8 -*-

 import sys

argvs = sys.argv
argc = len(argvs)

if(argc < 2):
    print "Usage: #python %s filename" % argvs[0]
    quit()


fname = argvs[1]

print "Step 1:Count File lines"
print sum([1 in open(filename)])

print "Step 2:Replace tab to space"
for line in open(fname):
    print line.replace("\t", " "),
print

print "Step 3:Cut line1 and line2"
foutCol1 = open("col1.txt", "w+")
foutCol2 = open("col2.txt", "w+")

for line in open(filename):
	cols = line.strip().split("\t")
	if len(col) < 2: continue
 	col1.write(col[0] + "\n")
    col2.write(col[1] + "\n")

col1.close()
col2.close()

print "Step4:Combine col1.txt and col2.txt"
foutCol = open("col.txt", "w+")
for col1, col2 in zip(open("col1.txt"), open("col2.txt")):
	foutCol.write("\t".join(col1, col2))
foutCol.close()

print "Step5:先頭" + argvs[2] + "行だけ表示"
headN = int(argvs[2])
from itertools import islice
with open(filename) as fin:
    for line in islice(fin, headN)


    
f = open(argvs[1])
 N = len(lines)
n = int(argvs[2])
for l in range(0, min(n, N)):
    print lines[l].strip()
print

print "Step6:最後" + argvs[2] + "行だけ表示"
for l in range(max(N - n, 0), N):
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
# リストの作成を行う
ls = []
for l in lines:
    col = l[:-1].split("\t")
    if len(col) > 1:
        ls.append(col)
print
ls.sort(key=lambda ls: ls[1])
for l in ls:
    print l
print

print "Step9:2列名-1列目をkeyとして降順にソート"
S
ls.sort(key=lambda ls: ls[1], reverse=False)
# key = itemgetter(1,2)でも可能か？
for l in ls:
    print l
print

print "Step10:1カラム目の出現頻度を調べ、出現頻度の高い順に並び替え、入力にはcol1.txtを用いる"
# cntをそのまま用いてソート
for k, v in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
    print k, v
print
