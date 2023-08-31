#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 024_number-addition-and-subtraction-game.py
@time: 2023/8/16 15:18
@project: huawei-od-python
@desc: 024 数字加减游戏
"""


def solve_method(s, t, a, b):
    diff = abs(s - t)
    min_count = 0
    while ((diff - min_count * a) % b != 0) and ((diff + min_count * a) % b != 0):
        min_count += 1
    return min_count


if __name__ == "__main__":
    assert solve_method(1, 10, 5, 2) == 1
    assert solve_method(11, 33, 4, 10) == 2
