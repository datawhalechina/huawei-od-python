#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-29 16:16:19
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$



def solve_method(n,m,arr):
	max_value= 0
	for start_row in range(n):
		for start_col in range(m):
			for end_row in range(start_row, n):
				sums = 0
				for end_col in range(start_col, m):
					row_index = end_row
					while  row_index >= start_row:
						sums += arr[row_index][end_col]
						row_index -= 1

					if sums <=0:
						break
					max_value = max(max_value, sums)

	return max_value





if __name__ == '__main__':

	assert solve_method(3,4,[[-3,5,-1,5],[2,4,-2,4],[-1,3,-1,3]]) == 20
	assert solve_method(3,4,[[-3,50,-10,-5],[-2,-4,-2,-4],[-1,-3,-1,-3]]) == 50
