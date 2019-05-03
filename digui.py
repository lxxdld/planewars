# -*- coding: GBK -*-
def move(n,a,b,c):
	if n==1:
		print(a,' --> ',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)#注意这里是1不是n
		move(n-1,b,a,c)
###要点 其实就是一个简单的分治法，在这个例子中就是：只管处理眼前的这个盘子。
move(3,"a","b","c")

"""
1.将上面n-1片圆盘从A移动到B上
2.将第n片圆盘从A移动到C上
3.将n-1片圆盘从B移动到C上
函数中，位置变量的位置才是盘的位置
"""
