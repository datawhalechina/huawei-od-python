#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 207_reassemble-the-string.py
@time: 2023/7/21 19:31
@project: huawei-od-python
@desc: 207 重组字符串
"""
import re


def convert(substring):
    upper = re.compile("[A-Z]")
    lower = re.compile("[a-z]")

    upper_count = len(upper.findall(substring))
    lower_count = len(lower.findall(substring))
    if lower_count > upper_count:
        return substring.lower()
    elif upper_count > lower_count:
        return substring.upper()

    return substring


def solve_method(k, line):
    strings = line.split("-")
    # 第一个子串直接转换并保存
    result = [convert(strings[0])]
    strings = "".join(strings[1:])
    # 每隔k个字符组成新的子串
    while len(strings):
        if len(strings) >= k:
            # 对子串进行转换
            result.append(convert(strings[:k]))
            strings = strings[k:]
        else:
            result.append(convert(strings))
            strings = ""
    # 用-拼接
    return "-".join(result)


if __name__ == '__main__':
    assert solve_method(3, "12abc-abCABc-4aB@") == "12abc-abc-ABC-4aB-@"
