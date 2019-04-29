# -*- coding: GBK -*-
height=float(input())
weight=float(input())
bmi=weight/(height*height)
if bmi<=17.5:
	print("过轻")
elif bmi>=18.5 and bmi<25:
	print("正常")
elif bmi>=25 and bmi<28:
	print("过重")
elif bmi>=28 and bmi<32:
	print("肥胖")
else:
	print("过度肥胖")
