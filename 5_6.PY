# -*- coding: GBK -*-
'''
def map(f,L):
	L = []
	for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
		L.append(f(n))
	print(L)
“把f(x)作用在list的每一个元素并把结果生成一个新的list”
'''

#输出大写的第一个字母
"""
def normalize(L1):
	L2=[]
	L2=L1[0].upper()+L1[1:].lower()
	return L2

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
for git
"""

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
from functools import reduce
def xx(x,y):#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
	return x*y
	
def prod(L):
	return (reduce(xx,L))
    
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
"""


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def fn(x,y):
	return x*10+y
def char2num(s):
   digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
   return digits[s]
   
def str2float(s):
	intnum=0
	floatnum=0
	for i in s:
		if i!='.':
			intnum=intnum+1
			if (len(s)-intnum-1)>0:
				floatnum=len(s)-intnum-1
			else :
				floatnum=0
		else :
			break#得出整数的长度和小数的长度
"""
	更好的的方法：
	for x, i in enumerate(s):
		if i == ".":
			numint = s[0:x]
			numfloat = s[x+1:]
			break
"""
	s1=s[:intnum]
	s2=s[-floatnum:]		
	return reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))*0.1**floatnum
	
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


