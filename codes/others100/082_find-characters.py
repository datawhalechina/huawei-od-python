#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 082_find-characters.py
@time: 2023/8/8 17:17
@project: huawei-od-python
@desc: 082 找字符
"""


def solve_method(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    return "".join(sorted(str1.intersection(str2)))


if __name__ == '__main__':
    assert solve_method("bach", "bbaaccddfg") == "abc"
    assert solve_method("fach", "bbaaccedfg") == "acf"
