#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 300_block-games-with-the-same-number.py
@time: 2023/8/1 18:52
@project: huawei-od-python
@desc: 300 相同数字的积木游戏
"""
from collections import defaultdict


def solve_method(nums):
    idx = defaultdict(list)

    for i in range(len(nums)):
        idx[nums[i]].append(i)

    ans = -1
    for k in idx.keys():
        if len(idx[k]) > 1:
            ans = max(ans, idx[k][-1] - idx[k][0])

    return ans


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 1, 4]) == 3
    assert solve_method([1, 2]) == -1
