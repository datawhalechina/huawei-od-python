#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 198_kick-stones.py
@time: 2023/8/27 1:32
@project: huawei-od-python
@desc: 198 踢石子问题
"""


def solve_method(n):
    nums = [i for i in range(1, 101)]
    max_index = len(nums) - 1
    index = 0
    count = 0
    num_n = 0
    while count < 98:
        while True:
            if index > max_index:
                index = 0
            if nums[index] != -1:
                num_n += 1
            if num_n == n:
                num_n = 0
                break
            index += 1
        count += 1
        nums[index] = -1

    for item in nums:
        if item != -1:
            print(item, end=" ")


k = int(input())
solve_method(k)
