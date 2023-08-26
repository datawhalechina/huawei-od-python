#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 186_english-input.py
@time: 2023/8/27 1:29
@project: huawei-od-python
@desc: 186 英文输入法
"""

import re


def solve_method(s, pre):
    words = re.findall(r'\w+', s)
    word_set = set(words)

    result = []

    for word in word_set:
        if word.startswith(pre):
            result.append(word)
    if not result:
        result.append(pre)

    print(' '.join(sorted(result)))


if __name__ == '__main__':
    s = input()
    pre = input()
    solve_method(s, pre)
