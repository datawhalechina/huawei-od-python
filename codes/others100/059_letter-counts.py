#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 059_letter-counts.py
@time: 2023/08/16 13:12
@project: huawei-od-python
@desc: 059 字母计数
"""
from collections import Counter


def solve_method(line):
    # 使用Counter计算每个字符的出现次数
    char_counter = Counter(line)

    # 按字母出现次数从大到小，如果相等，按照自然顺序排序，小写字母在前，大写字母在后
    char_count_pairs = sorted(char_counter.items(), key=lambda x: (-x[1], x[0].isupper()))

    result = ""
    for char, count in char_count_pairs:
        # 每个字符及其出现次数
        result += f"{char}:{count};"

    return result


if __name__ == "__main__":
    assert solve_method("xyxyXX") == "x:2;y:2;X:2;"
    assert solve_method("abababb") == "b:4;a:3;"
