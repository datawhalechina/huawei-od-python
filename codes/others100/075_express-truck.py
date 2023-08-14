#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 075_express-truck
@time:  14/8/2023 上午 9:25
@project:  huawei-od-python 
"""
import sys


def solve_method(weight, capacity):
    weight = sorted(weight)
    count, total_weight = 0, 0
    for i in range(len(weight)):
        total_weight += weight[i]
        if total_weight <= capacity:
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    weight = list(map(int, sys.stdin.readline().strip().split(',')))
    capacity = int(sys.stdin.readline().strip())
    res = solve_method(weight, capacity)
    print(res)
