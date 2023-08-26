#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 194_street-lighting.py
@time: 2023/8/27 1:31
@project: huawei-od-python
@desc: 194 路灯照明
"""


def main():
    n = int(input())
    ints = list(map(int, input().split()))
    solve_method(ints)


def solve_method(ints):
    bytes_ = bytearray((len(ints) - 1) * 100)

    for i in range(len(ints)):
        pos = i * 100
        left = max(pos - ints[i], 0)
        right = min(pos + ints[i], len(bytes_))

        for k in range(left, right):
            bytes_[k] = 1

    count = bytes_.count(0)
    print(count)


main()
