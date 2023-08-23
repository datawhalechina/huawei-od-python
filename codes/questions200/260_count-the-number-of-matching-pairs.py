#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 260_count-the-number-of-matching-pairs.py
@time: 2023/8/22 16:58
@project: huawei-od-python
@desc: 260 统计匹配的二元组个数
"""
from collections import Counter


def solve_method(A, B):
    dict_A = Counter(A)
    dict_B = Counter(B)

    count = 0
    for key in dict_A:
        if key in dict_B:
            count += dict_A[key] * dict_B[key]
    return count


if __name__ == "__main__":
    # 5
    # 4
    # 1 2 3 4 5
    # 4 3 2 1
    # M = int(input().strip())
    # N = int(input().strip())
    # A = list(map(int, input().strip().split()))
    # B = list(map(int, input().strip().split()))
    # print(solve_method(A, B))

    assert solve_method([1, 2, 3, 4, 5], [4, 3, 2, 1]) == 4
    assert solve_method([1, 2, 4, 4, 2, 1], [1, 2, 3]) == 4
