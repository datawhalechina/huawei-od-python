#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 273_rearrange-string.py
@time: 2023/7/13 14:23
@project: huawei-od-python
@desc: 273 字符串重新排序
"""
from collections import defaultdict


def solve_method(string):
    words = string.split()
    word_freqs = defaultdict(int)
    for word in words:
        rearrange_word = "".join(sorted(word))
        word_freqs[rearrange_word] += 1

    sorted_freqs = sorted(word_freqs.items(),
                          key=lambda x: (-x[1], len(x[0]), x[0]))

    result = []
    for (word, freqs) in sorted_freqs:
        result.extend([word] * freqs)

    result = " ".join(result)
    return result


if __name__ == '__main__':
    assert solve_method("This is an apple") == "an is This aelpp"
    assert solve_method("My sister is in the house not in the yard") \
           == "in in eht eht My is not adry ehosu eirsst"
