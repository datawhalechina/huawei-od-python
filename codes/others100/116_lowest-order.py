#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 16:14:43
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$

#import os



def solve_method(line):
	list_ = line.split(",")

	list_.sort(key=lambda x: int(x[-1]))
	return ",".join(list_)


if __name__ == '__main__':

	assert solve_method("1,2,5,-21,22,11,55,-101,42,8,7,32") == "1,-21,11,-101,2,22,42,32,5,55,7,8"