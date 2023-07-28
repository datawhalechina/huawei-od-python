#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jack Lee C.S.
@file: 291_Maximum-Number-of-Substrings-Extracted
@time: 2023/07/12 10:59
@project: huawei-od-python
@desc: 291_Maximum-Number-of-Substrings-Extracted
@tags: String-Matching
"""
def solution(A:list, B:list)->int:
	# ababcecfdc
	# abc
	res = 0
	exist = [True for _ in range(len(A))] # -1:removed
	flg = True # Find one pair?
	while flg: # not null
		flg = False
		ib = 0
		for ia in range(len(A)):
			if exist[ia]: # exist
				if A[ia] == B[ib]: # match 
					ib += 1 # move forward
					exist[ia] = False # remove 
				ia += 1 # move 

			if ib == len(B): # reach end of B
				res += 1
				flg = True
				break
	return res

if __name__ == '__main__':
    assert solution('ababcecfdc', 'abc') == 2