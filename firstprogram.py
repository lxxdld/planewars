# -*- coding: GBK -*-
height=float(input())
weight=float(input())
bmi=weight/(height*height)
if bmi<=17.5:
	print("����")
elif bmi>=18.5 and bmi<25:
	print("����")
elif bmi>=25 and bmi<28:
	print("����")
elif bmi>=28 and bmi<32:
	print("����")
else:
	print("���ȷ���")
