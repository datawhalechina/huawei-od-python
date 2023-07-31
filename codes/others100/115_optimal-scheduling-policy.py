#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-31 15:30:29
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os
def solve_method(arr):
	
	res = 0
	preIndex = None
	for i in range(len(arr)):
		times = list(map(int, arr[i].split()))
		if preIndex == None:

			minTime = min(times)
			preIndex = times.index(minTime)
			
			if  minTime in  times[:preIndex] + times[preIndex + 1:]:
				
				preIndex = None  
		else:
			minTime = min(times[:preIndex] + times[preIndex + 1:])
			preIndex = times.index(minTime)
			
			if   minTime in  times[:preIndex] + times[preIndex + 1:]:	
				preIndex = None 
		res += minTime
	return res
if __name__ == '__main__':

	solve_method(["15 8 17","9 20 9","5 7 11"])==8+9+5
	solve_method(["15 8 17","12 20 9","5 7 11"])==8+9+11
