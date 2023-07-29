#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 060_string-encryption
@time:  29/7/2023 下午 11:55
@project:  huawei-od-python 
"""


def solve_method(strings):
    a = [1, 2, 4]
    offsets = [0] * 50
    for i in range(50):
        if i < 3:
            offsets[i] = a[i]
        else:
            offsets[i] = offsets[i - 1] + offsets[i - 2] + offsets[i - 3]
    chars = list(strings)
    for i in range(len(chars)):
        c = chars[i]
        chars[i] = chr((ord(c) - 97 + offsets[i]) % 26 + 97)
    return ''.join(chars)


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        strings = input().strip()
        res = solve_method(strings)
        print(res)
