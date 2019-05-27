s='123456.789'
intnum=0
floatnum=0
for i in list(s):
	if i!='.':
		intnum=intnum+1
		if (len(s)-intnum-1)>0:
			floatnum=len(s)-intnum-1
		else :
			floatnum=0
	else :
		break
print(intnum,'+',floatnum)
print(s[:intnum],'+',s[-floatnum:])
