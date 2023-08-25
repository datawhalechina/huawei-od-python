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
    nums = sorted(nums)
    ans = 0
    sum_weight = 0
    for i in range(len(nums)):
        sum_weight += nums[i]
        if sum_weight > weight:
            return ans
        else:
            ans += 1
    return ans


if __name__ == '__main__':
    nums = list(map(int, input().strip().split(',')))
    weight = int(input().strip())
    res = solve_method(nums, weight)
    print(res)
