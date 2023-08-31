#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 041_the-boxes-are-arranged-in-a-zigzag-pattern.py
@time: 2023/8/2 10:52
@project: huawei-od-python
@desc: 041 箱子之字形摆放
"""


def solve_method(chars, n):
    result = ["" for _ in range(n)]
    index = 0
    # 标识：True表示从上到下，False表示从下到上
    asc = True

    for c in chars:
        if index == -1:
            index = 0
            asc = True
        if index == n:
            index = n - 1
            asc = False
        result[index] += c

        if asc:
            index += 1
        else:
            index -= 1

    return result


if __name__ == '__main__':
    assert solve_method("ABCDEFG", 3) == ["AFG", "BE", "CD"]
