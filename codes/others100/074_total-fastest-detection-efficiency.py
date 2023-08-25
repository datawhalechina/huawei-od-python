#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 074_total-fastest-detection-efficiency
@time:  2023/8/24 16:42
@project:  huawei-od-python
@desc: 074 总最快检测效率
"""


def solve_method(nums, num_volunteer):
    profit = []
    for p in nums:
        profit.extend([p * 0.2, p * 0.1, p * 0.1, p * 0.1])
    nums = [i * 0.8 for i in nums]
    return int(sum(nums) + sum(sorted(profit, reverse=True)[:num_volunteer]))


if __name__ == '__main__':
    n1, n2 = map(int, input().strip().split(' '))
    nums = list(map(int, input().strip().split(' ')))
    res = solve_method(nums, n2)
    print(res)
