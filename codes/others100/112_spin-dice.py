#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 112_spin-dice.py
@time: 2023-07-28 12:09:14
@project: huawei-od-python
@desc: 112 骰子旋转
"""


def solve_method(line):
    res = ['1', '2', '3', '4', '5', '6']

    roll_switch = {
        "L": lambda: roll(res, 0, 2, 4, 6),
        "R": lambda: roll(res, 4, 6, 0, 2),
        "F": lambda: roll(res, 2, 4, 4, 6),
        "B": lambda: roll(res, 4, 6, 2, 4),
        "A": lambda: roll(res, 2, 4, 0, 2),
        "C": lambda: roll(res, 0, 2, 2, 4)
    }
    for c in line:
        roll_switch[c]()
        print(res)

    return "".join(res)


def roll(res, s1, e1, s2, e2):
    res[s1:e1], res[s2:e2] = res[s2:e2], res[s1:e1][::-1]
    return res


if __name__ == "__main__":
    assert solve_method("LR") == "123456"
    # assert solve_method("FCR") == "342156"
