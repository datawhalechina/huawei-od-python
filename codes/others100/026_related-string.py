#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 026_related-string.py
@time: 2023/8/7 16:21
@project: huawei-od-python
@desc: 026 关联字串
"""
from collections import Counter


def solve_method(str1, str2):
    length = len(str1)
    for i in range(len(str2) - length + 1):
        sub_str = list(str2[i:i + length])
        if Counter(sub_str) == Counter(str1):
            return i
    return -1


if __name__ == '__main__':
    assert solve_method("abc", "efghicabiii") == 5
    assert solve_method("abc", "efghicaibii") == -1
