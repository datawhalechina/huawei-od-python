#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 270_reverse-words.py
@time: 2023/7/12 14:35
@project: huawei-od-python
@desc: 270 单词倒序
"""


def solve_method(line):
    result = ""
    # 使用临时字符串记录单词
    words = ""
    for char in line:
        if char.isalpha():
            words += char
        else:
            # 将单词逆序
            result += words[::-1]
            words = ""
            result += char

    return result


if __name__ == '__main__':
    s = "yM eman si boB."
    assert solve_method(s) == "My name is Bob."

    s = "woh era uoy ? I ma enif."
    assert solve_method(s) == "how are you ? I am fine."
