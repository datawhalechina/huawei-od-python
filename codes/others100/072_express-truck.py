#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 072_express-truck
@time:  2023/8/24 11:58
@project:  huawei-od-python
@desc: 072 快递货车
"""


def solve_method(nums, weight):
    nums.sort()
    count = 0
    sum_weight = 0
    for i in range(len(nums)):
        sum_weight += nums[i]
        if sum_weight > weight:
            return count
        else:
            count += 1
    return count


if __name__ == '__main__':
    assert solve_method([5, 10, 2, 11], 20) == 3
