# -*- coding: GBK -*-
#first type of loop
names = ["lian","lin","li"]
for name in names:
	print(name)
#range(101) can make a list from 0 to 100 (<101)

#计算5050
summ = 0
for i in range(101):
	summ +=i
print (summ)
	
summ = 0
i=0
while i<=100:
	summ+=i
	i=i+1
print(summ)
