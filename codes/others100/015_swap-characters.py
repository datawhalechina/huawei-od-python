#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 015_swap-characters.py
@time: 2023/7/26 20:37
@project: huawei-od-python
@desc: 015 交换字符
"""


def solve_method(string):
    string = list(string)
    pos = 0
    min_char = string[0]
    for i in range(1, len(string)):
        char = string[i]
        if char <= min_char:
            min_char, pos = char, i

    if pos != 0:
        string[pos], string[0] = string[0], min_char

    return "".join(string)


if __name__ == '__main__':
    assert solve_method("abcdef") == "abcdef"
    assert solve_method("bcdefa") == "acdefb"
