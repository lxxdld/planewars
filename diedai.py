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
    
# ����
if findMinAndMax([]) != (None, None):
    print('����ʧ��1!')
elif findMinAndMax([7]) != (7, 7):
    print('����ʧ��2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('����ʧ��3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('����ʧ��4!')
else:
    print('���Գɹ�5!')
