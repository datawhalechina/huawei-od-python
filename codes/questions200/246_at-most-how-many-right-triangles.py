#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 246_at-most-how-many-right-triangles.py
@time: 2023/8/18 9:22
@project: huawei-od-python
@desc: 246 最多几个直角三角形
"""
import math
from collections import Counter


def solve_method(arr):
    result = []
    for nums in arr:
        nums = nums[1:]

        count = 0
        counter = Counter(nums)
        num_keys = list(counter.keys())
        for i in range(len(num_keys)):
            for j in range(i + 1, len(num_keys)):
                a = num_keys[i]
                b = num_keys[j]
                if counter[a] > 0 and counter[b] > 0:
                    c = math.sqrt(a ** 2 + b ** 2)
                    if c in num_keys and counter[c] > 0:
                        counter[a] -= 1
                        counter[b] -= 1
                        counter[c] -= 1
                        count += 1
        result.append(count)
    return result


if __name__ == "__main__":
    arr = [[7, 3, 4, 5, 6, 5, 12, 13]]
    assert solve_method(arr) == [2]

    arr = [[7, 3, 4, 5, 6, 6, 12, 13]]
    assert solve_method(arr) == [1]
