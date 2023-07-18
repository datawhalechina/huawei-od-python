#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 134_the-longest-consecutive-substring.py
@time: 2023/7/18 22:50
@project: huawei-od-python
@desc: 134 最长连续子串
"""
import re


def solve_method(line):
    # 使用双指针
    start = 0
    end = 1
    max_length = -1
    # 设置正则表达式
    p = re.compile("[a-zA-Z]")
    while start < len(line) and end < len(line):
        end += 1
        sub_str = line[start:end]
        # 判断子串中是否只有一个字母
        if len(p.findall(sub_str)) == 1:
            max_length = max(max_length, len(sub_str))
        else:
            # 扩大范围
            start += 1

    return max_length


if __name__ == '__main__':
    assert solve_method("abC124ACb") == 4
    assert solve_method("a5") == 2
    assert solve_method("aBB9") == 2
    assert solve_method("abcdef") == -1
    assert solve_method("a12b234g1234") == 8
