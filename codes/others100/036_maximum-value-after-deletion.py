#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 036_maximum-value-after-deletion.py
@time: 2023/8/8 10:28
@project: huawei-od-python
@desc: 036 删除重复数字后的最大数字
"""
from collections import Counter


def backstracking(nums: list, paths: list):
    num_count = Counter(nums)
    # 当所有频数都为1时，可得到消除重复的数字
    if all([True if x[1] == 1 else False for x in num_count.items()]):
        paths.append(int("".join(nums)))
        return

    for i, num in enumerate(nums):
        if num_count[num] > 1:
            nums.pop(i)
            backstracking(nums, paths)
            nums.insert(i, num)


def solve_method(num):
    nums = list(str(num))
    paths = []
    backstracking(nums, paths)

    return max(paths)


if __name__ == '__main__':
    assert solve_method(12341) == 2341
    assert solve_method(42234) == 423
