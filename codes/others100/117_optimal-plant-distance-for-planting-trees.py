#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 16:32:22
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os

def solve_method(holes, target):
	holes.sort()
	left = 0
	right = holes[-1] - holes[0]
	answer = -1 

	while left <= right:
		mid = left + (right - left) // 2
		count =1 
		previous = holes[0]
		for i in range(1, len(holes)):
			if holes[i] - previous >= mid:
				count += 1
				previous = holes[i]

				if count >= target:
					answer = mid
					left = mid +1 
					break


		if count < target:
			right= mid - 1

	return answer




if __name__ == '__main__':

	assert solve_method([1,3,6,7,8,11,13],3) == 6
	assert solve_method([1,2,6,8,14],3) == 6
	assert solve_method([1,7,14],2) == 13