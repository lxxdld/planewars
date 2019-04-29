# -*- coding: GBK -*-
resource=['a','a','b','a','b','c']
resource1=['a','a','b','a','b','c','D','D']
#dict字典是用空间换取时间
#方法get(),如果key不存在，可以返回None，或者自己指定的value：
dic={}
dic1={}
for element in resource:
	result=dic.get(element,-1)
	if result==-1:#dic中不存在element
		dic[element]=1#放入dic中，val为1
	else :
		dic[element]+=1
print(dic)
i=0		
for element in resource1:
	result=dic1.get(element)
	if not result:#没出现过
		dic1[element]=1
	else :#出现过
		dic1[element]+=1
print(dic1)		
		
