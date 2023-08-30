#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 060_string-encryption.py
@time:  2023/7/29 23:55
@project:  huawei-od-python
@desc: 060 字符串加密
"""


def solve_method(strings):
    offsets = [0] * 50
    offsets[0:2] = [1, 2, 4]
    for i in range(3, 51):
        offsets[i] = offsets[i - 1] + offsets[i - 2] + offsets[i - 3]

    result = []
    for chars in strings:
        chars = list(chars)
        for i in range(len(chars)):
            c = chars[i]
            chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)
        result.append("".join(chars))
    return result


if __name__ == '__main__':
    assert solve_method(["xy"]) == ["ya"]
    assert solve_method(["xyabcdef", "abcdefghijk"]) == ["yaeipbwi", "bdgkrdykbxu"]
