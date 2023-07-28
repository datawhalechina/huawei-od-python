#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2023-07-28 15:07:36
# @Author  : catcooc 
# @email   ： 
# @Link    : https://github.com/catcooc
# @Version : $Id$



def solve_method(times):
	sorted_times = sorted(times, key=get_time)
	return sorted_times



def get_time(time_str: str):
	h = int(time_str.split(':')[0])
	m = int(time_str.split(':' )[1])
	s = int(time_str.split(':')[-1].split('.')[0])
	n = int(time_str.split(':')[-1].split('.')[1])
	return h *60 * 60 * 1000 + m * 60 *1000 + s * 1000 +n


if __name__ == '__main__':
	assert solve_method(["01:41:8.9","1:1:09.211"]) == ["1:1:09.211","01:41:8.9"]
	assert solve_method(["23:41:08.023","1:1:09.211","08:01:22.0"]) == ["1:1:09.211","08:01:22.0","23:41:08.023"]
	assert solve_method(["22:41:08.023","22:41:08.23"]) == ["22:41:08.023","22:41:08.23"]
