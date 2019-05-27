	# -*- coding: GBK -*-
def findMinAndMax(L):
	if len(L)!=0:
		big=L[0]
		small=L[0]
		for x in L:
			if big < x:
				big = x
			if small > x:
				small = x
		return (small,big)
	else:
		return (None, None)
    
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功5!')
