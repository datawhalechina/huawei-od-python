#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 182_archaeologist.py
@time: 2023/8/27 1:26
@project: huawei-od-python
@desc: 182 考古学家
"""

import itertools


def solve_method(fragments):
    fragments = list(itertools.permutations(fragments))
    fragments = list(set(["".join(i) for i in fragments]))
    fragments.sort()
    return fragments


if __name__ == '__main__':
    assert solve_method(["a", "b", "c"]) == ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert solve_method(["a", "b", "a"]) == ["aab", "aba", "baa"]
    assert solve_method(["a", "b", "ab"]) == ["aabb", "abab", "abba", "baab", "baba"]
