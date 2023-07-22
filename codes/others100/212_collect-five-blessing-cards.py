#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 212_collect-five-blessing-cards.py
@time: 2023/7/22 21:58
@project: huawei-od-python
@desc: 212 集五福
"""


def solve_method(arr):
    result = [0] * 5

    for cards in arr:
        for i in range(5):
            if cards[i] == "1":
                result[i] += 1

    return min(result)


if __name__ == '__main__':
    assert solve_method(["11001", "11101"]) == 0
    assert solve_method(["11101", "10111"]) == 1
