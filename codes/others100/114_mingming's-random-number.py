#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 15:49:08
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os

def solve_method(lst):
	lst= list(set(lst))
	lst.sort
	return lst



if __name__ == '__main__':
	assert solve_method([2,2,1]) == [1,2]
	assert solve_method([3,6,9,8,2,1,1,9,8]) == [1,2,3,6,8,9]