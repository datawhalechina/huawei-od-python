#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-26 10:22:50
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#

import heapq
def parse_array(line):
	return list(map(int, line.strip().split()))

def solve_method_1(arr1, arr2 , k):
	arr1=parse_array(arr1)
	arr2=parse_array(arr2)
	k=int(k)
	#计算最大需要相加到数组的范围
	len_addarr1=min(k+1,arr1[0]+1)
	len_addarr2=min(k+1,arr2[0]+1)
	#如果含有长度为一的数组我们直接返回取该数组元素和另一个数组前k个元素的相加
	if arr1[0]==1:
		return arr1[1]*k+sum(arr2[1:len_addarr2])
	elif arr2[0]==1:
		return arr2[1]*k+sum(arr1[1:len_addarr1])
	sums = []
	for x in arr1[1:len_addarr1]:
		for  y  in arr2[1:len_addarr2]:
			heapq.heappush(sums,x + y)
			
			
	res = 0
	for i in range(k):
		res += heapq.heappop(sums)
	return (res)

from collections import Counter

def solve_method_2(arr1, arr2 , k):
	arr1=parse_array(arr1)
	arr2=parse_array(arr2)
	k=int(k)
	#调换数组顺序为了后面用短数组排序
	if arr1[0]> arr2[0]:
		arr1 , arr2=arr2 , arr1

	len_addarr1=min(k+1,arr1[0]+1)
	
	#调换数组顺序为了后面遍历用短数组因为无论k多大都是短的数组先被抽取
	if arr1[0]==1:
		return k*arr1[1]+sum(arr2[1:k+1])

	arr2_position=1
	res=0
#优先计数前面的数
	for num, num_count in Counter(arr1[1:]).items():
		if k -num_count*arr2[0] <= 0 :
			remainder,quotient=k%num_count,k//num_count
			if remainder==0:
				res += (num*quotient+sum(arr2[1:1+quotient]))*(num_count)
			else:
				
				
				res += (num*quotient+sum(arr2[1:1+quotient]))*(num_count)+(num+arr2[quotient+remainder])*(k-num_count*(quotient))
			
			return res

		res += (num +arr2[1:])*num_count
		k-=num_count*arr2[0]


	return (res)




if __name__ == "__main__":
	solve_methods = [solve_method_1, solve_method_2]


	for solve_method in solve_methods:
		assert solve_method("1 1","3 1 2 3" ,"2") == 5 
		assert solve_method("3 1 1 2","3 1 2 3" ,"2") == 4 
		assert solve_method("3 1 1 1","3 1 2 3" ,"3") == 6
		assert solve_method("3 1 1 ","3 1 2 3" ,"5") == 14
		assert solve_method("3 1 1 ","3 1 2 3" ,"6") == 18
		assert solve_method("3 1 2 3 4 ","3 1 2 3" ,"2") == 5