#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 048_bit-error-rate.py
@time: 2023/8/3 16:51
@project: huawei-od-python
@desc: 048 通信误码
"""
import math
from collections import defaultdict


def solve_method(arr):
    # 构建误码索引字典，key为误码值，value为该值所在的位置
    num_index = defaultdict(list)

    for i in range(len(arr)):
        num_index[arr[i]].append(i)

    max_count = 0
    min_len = math.inf

    for values in num_index.values():
        count = len(values)
        length = values[-1] - values[0] + 1

        # 如果出现次数较大，或次数相同时，距离较小，则记录最大出现次数和最小距离。
        if count > max_count or (count == max_count and length < min_len):
            max_count = max(count, max_count)
            min_len = min(length, min_len)

    return min_len


if __name__ == '__main__':
    assert solve_method([1, 2, 2, 4, 1]) == 2
    assert solve_method([1, 2, 2, 4, 2, 1, 1]) == 4
