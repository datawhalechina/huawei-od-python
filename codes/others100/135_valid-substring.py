#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 135_valid-substring.py
@time: 2023/7/18 23:34
@project: huawei-od-python
@desc: 135 有效子字符串
"""


def solve_method(s, l):
    last_valid_index = -1
    for ch in s:
        # 判断有效位置是否还在L长度范围内
        while last_valid_index < len(l) - 1:
            last_valid_index += 1
            # 判断S中的字符是否等于L中的字符
            if ch == l[last_valid_index]:
                # 如果相等，则跳出while循环，继续遍历S字符串
                break
        else:
            # 当有效位置已经超过了L长度范围，但S字符串还有字符，直接跳出遍历
            last_valid_index = -1
            break
    return last_valid_index


if __name__ == '__main__':
    assert solve_method("ace", "abcde") == 4
    assert solve_method("fgh", "abcde") == -1
    assert solve_method("acce", "abcdec") == -1
