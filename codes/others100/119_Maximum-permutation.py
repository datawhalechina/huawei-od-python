#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-30 18:22:36
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

def solve_method(nums):
	nums=nums.split(" ")
	nums.sort(reverse=True)
	print(list(map(lambda num: num * 3,nums)))

	return "".join (nums)

if __name__ == '__main__':

	assert solve_method("10 9") == '910'

