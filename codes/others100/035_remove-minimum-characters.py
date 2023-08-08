#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 035_remove-minimum-characters.py
@time: 2023/8/8 10:18
@project: huawei-od-python
@desc: 035 删除最少的字符
"""
from collections import Counter


def solve_method(chars):
    # 统计字符频率
    freq = Counter(chars)
    # 求最小值
    min_freq = min(freq.values())
    result = ""
    for c in chars:
        if freq[c] != min_freq:
            result += c

    if len(result) == 0:
        return 'empty'
    return result


if __name__ == '__main__':
    assert solve_method("abcdd") == "dd"
    assert solve_method("aabbccdd") == "empty"
