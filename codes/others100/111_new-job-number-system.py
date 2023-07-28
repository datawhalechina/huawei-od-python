#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 11:33:18
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os
import math


def solve_method(x,y):

	cb = math.pow(26, y)

	if cb >= x:
		return 1
	else:
		return math.ceil(math.log(x/cb,10))

if __name__ == "__main__":
	
	assert solve_method(260,1) == 1
	assert solve_method(26,1) == 1
	assert solve_method(2600,1) == 2
	assert solve_method(27,1) == 1
	assert solve_method(2601,1) == 3