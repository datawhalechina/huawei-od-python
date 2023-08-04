#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 119_maximum-permutation.py
@time: 2023-07-30 18:22:36
@project: huawei-od-python
@desc: 119 最大排列
"""


def solve_method(nums):
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                nums[i], nums[j] = nums[j], nums[i]

    return int("".join(nums))


if __name__ == '__main__':
    assert solve_method(["10", "9"]) == 910
