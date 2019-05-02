# -*- coding: GBK -*-
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0ax 
#2+bx+c=0 的两个解。
import math
def quadratic(a,b,c):
	if (b*b-4*a*c)<0:
		print("no resule")
		return 0
	else:	
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return x1,x2
meiling={"mei":"xing","ling":"ling"}
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
print(meiling["mei"])
