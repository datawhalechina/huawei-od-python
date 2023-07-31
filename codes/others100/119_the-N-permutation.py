#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-31 15:01:53
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os
import itertools

def solve_method(n, k):
	arr = [i + 1 for i in range(n)]
	perms = list(itertools.permutations(arr))
	res = int("".join(str(x) for x in perms[k - 1]))
	return res

if __name__ == '__main__':

	assert solve_method(2,2) == 21