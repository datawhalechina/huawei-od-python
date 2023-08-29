#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 067_search-continuous-scope
@time:  2023/8/13 23:38
@project:  huawei-od-python
@desc: 067 寻找连续区间
"""


def solve_method(nums, target):
    n = len(nums)
    count = 0
    if sum(nums) < target:
        return count
    for i in range(n):
        for j in range(i, n):
            if sum(nums[i:j + 1]) >= target:
                count += 1
    return count


if __name__ == '__main__':
    assert solve_method([3, 4, 7], 7) == 4
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10000) == 0
