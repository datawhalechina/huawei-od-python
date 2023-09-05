#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 049_enhanced-strstr.py
@time: 2023/9/3 23:18
@project: huawei-od-python
@desc: 049 增强的strstr
"""
import re


def solve_method(haystack, needle):
    match = re.search(needle, haystack)
    return match.start() if match else -1


if __name__ == '__main__':
    assert solve_method("abcd", "b[cd]") == 1
    assert solve_method("aabcdefg", "b[cd]d[eg]") == 2
