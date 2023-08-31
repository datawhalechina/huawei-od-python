#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 018_finding-similar-words.py
@time: 2023/8/19
@project: huawei-od-python
@desc: 018 寻找相似单词
"""
from collections import Counter


def solve_method(words, target_word):
    result = []
    for word in words:
        if Counter(word) == Counter(target_word):
            result.append(word)

    result.sort()
    return result if len(result) != 0 else "null"


if __name__ == '__main__':
    words = ["abc", "dasd", "tad", "bca"]
    assert solve_method(words, "abc") == ["abc", "bca"]

    assert solve_method(words, "abd") == "null"
