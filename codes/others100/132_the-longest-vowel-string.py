#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 132_the-longest-vowel-string.py
@time: 2023/7/18 21:34
@project: huawei-od-python
@desc: 132 最长的元音字符串
"""
import re


def solve_method(string):
    p = re.compile("[aeiouAEIOU]+")
    result = p.findall(string)
    result.sort(key=lambda x: len(x), reverse=True)
    return len(result[0]) if len(result) != 0 else 0


if __name__ == '__main__':
    assert solve_method("asdbuiodevauufgh") == 3
    assert solve_method("fgh") == 0
