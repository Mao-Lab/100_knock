#coding UTF-8

fr_col2 = open("col2.txt","r")
fw_col2 = open("col2_sort.txt","w+")

lines = fr_col2.readlines()

lines.sort()
print (lines)
fw_col2.writelines(lines)

fr_col2.close()
fw_col2.close()