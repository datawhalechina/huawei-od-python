#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 294_leftmost-redundant-overlay-substring.py
@time: 2023/7/31 20:38
@project: huawei-od-python
@desc: 294 最左侧冗余覆盖子串
"""
from collections import Counter


def solve_method(s1, s2, k):
    c1 = Counter(s1)
    for i in range(len(s2) - len(s1) - k):
        c2 = Counter(s2[i:i + len(s1) + k])
        if c1 < c2:
            return i

    return - 1


if __name__ == '__main__':
    assert solve_method("ab", "aabcd", 1) == 0
    assert solve_method("abc", "dfs", 10) == -1
