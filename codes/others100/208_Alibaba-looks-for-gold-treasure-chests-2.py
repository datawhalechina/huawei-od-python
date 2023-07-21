#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 208_Alibaba-looks-for-gold-treasure-chests-2.py
@time: 2023/7/22 0:16
@project: huawei-od-python
@desc: 208 阿里巴巴找黄金宝箱（2）
"""
from collections import defaultdict


def solve_method(nums):
    half = len(nums) // 2
    num_freq = defaultdict(int)

    for num in nums:
        num_freq[num] += 1

    num_freq = sorted(num_freq.items(), key=lambda x: -x[1])
    count = 0
    result = 0
    while count < half:
        count += num_freq[result][1]
        result += 1

    return result


if __name__ == '__main__':
    assert solve_method([6, 6, 6, 6, 3, 3, 3, 1, 1, 5]) == 2
    assert solve_method([1, 1, 1, 1, 3, 3, 3, 6, 6, 8]) == 2
    assert solve_method([2, 2, 2, 2]) == 1
