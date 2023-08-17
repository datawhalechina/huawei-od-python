#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 179_meet-rules-combination.py
@time: 2023/8/8 23:44
@project: huawei-od-python
@desc: 179 满足规则的组合
"""

from collections import Counter


def solve_method(n, nums):
    num_freq = Counter(nums)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            a = nums[i]
            b = nums[j]
            num_freq[a] -= 1
            num_freq[b] -= 1
            k = a - b
            if k % 2 == 0 and k // 2 in num_freq and num_freq[k // 2] > 0:
                return [a, b, (k // 2)]
            num_freq[a] += 1
            num_freq[b] += 1
    return 0


if __name__ == '__main__':
    assert solve_method(4, [2, 7, 3, 0]) == [7, 3, 2]
    assert solve_method(3, [1, 1, 1]) == 0
