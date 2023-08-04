#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 119_the-N-permutation.py
@time: 2023-07-31 15:01:53
@project: huawei-od-python
@desc: 119 第N个排列
"""
import itertools


def solve_method(n, k):
    arr = [i + 1 for i in range(n)]
    perms = list(itertools.permutations(arr))
    result = int("".join(str(x) for x in perms[k - 1]))
    return result


if __name__ == '__main__':
    assert solve_method(3, 3) == 213
    assert solve_method(2, 2) == 21
