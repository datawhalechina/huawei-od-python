#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 295_min-board-length.py
@time: 2023/7/31 21:45
@project: huawei-od-python
@desc: 295 最短木板长度
"""


def solve_method(m, A):
    N = len(A)
    A.sort()
    i = 0
    for j in range(m):
        # 补上最短的
        A[i] += 1
        if i == (N - 1) or A[i + 1] >= A[i]:
            # 如果当前依然是最短的，则继续让最短的加1
            i = 0
        else:
            # 如果后面那个更短，则向后比较
            i += 1
    return sorted(A)[0]


if __name__ == '__main__':
    assert solve_method(3, [4, 5, 3, 5, 5]) == 5
    assert solve_method(2, [4, 5, 3, 5, 5]) == 4
    assert solve_method(10, [4, 5, 5, 5, 5]) == 6
