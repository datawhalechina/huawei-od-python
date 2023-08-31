#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 038_knowledge-graph-neologism-mining.py
@time: 2023/8/2 9:06
@project: huawei-od-python
@desc: 038 知识图谱新词挖掘
"""
from collections import Counter


def solve_method(content: str, word: str) -> int:
    w = len(word)
    count = 0
    c2 = Counter(word)

    for i in range(len(content) - w + 1):
        c1 = Counter(content[i:i + w])
        if c1 == c2:
            count += 1

    return count


if __name__ == '__main__':
    assert solve_method("qweebaewqd", "qwe") == 2
    assert solve_method("abab", "ab") == 3
