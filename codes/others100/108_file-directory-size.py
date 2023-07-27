#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-27 14:30:46
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os
def mysplit(string):
	"""
	逗号分隔的数字字符串解析为整数列表

	Parameters :
		string (str): 逗号分隔的数字字符串，带有方括号
	Returns:
		result (list): 解析得到的整数列表
	"""
	result = []
	trimmed_str = string[1:-1] # 除字符串的首尾方括号
	if not trimmed_str:

		return result
	trimmed_str=trimmed_str.split(",")
	result=list(map(int ,trimmed_str))
	return result



def dfs (n,data_map):
	"""
	深度优先搜索函数，计算给定节点 n 的结果
	
	Parameters:n (int): 
		n (int): 节点值


	Returns:
		result (int): 计算得到的结果

	"""

	result = 0
	if n in data_map:
		 data = data_map[n]
		 result = data[0]
		 for i in range(1, len(data)):
		 	result += dfs(data[i],data_map)
	return result

def solve_method(m,n,dirs):
	data_map = {}
	#m, n = map(int, input().split())
    # 循环读取 m 行 数据
	for i in range(m):
		a, b, c= dirs[i].split()
		a = int(a)
		b = int(b)
		data_map.setdefault(a, [b] + mysplit(c))#.extend([b] + mysplit(c))

	print(data_map)
	res = dfs(n,data_map)
	#print(res)
	return res


if __name__ == "__main__":
	m,n= 3,1 
	dirs=["3 15 ()","1 20 (2)","2 10 (3)"]
	assert	solve_method(m,n,dirs)==45
	m,n= 4,2 
	dirs=["4 20 ()","5 30 ()","2 10 (4,5)","1 40 ()"]
	assert	solve_method(m,n,dirs)==60
	