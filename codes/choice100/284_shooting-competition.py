#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 284_shooting-competition.py
@time: 2023/7/14 17:22
@project: huawei-od-python
@desc: 284 投篮大赛
"""


def solve_method(ops):
    scores = []
    try:
        for op in ops:
            if op == "C":
                if len(scores) < 1:
                    raise ValueError
                scores.pop()
            elif op == "D":
                if len(scores) < 1:
                    raise ValueError
                scores.append(2 * scores[-1])
            elif op == "+":
                if len(scores) < 2:
                    raise ValueError
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(op)

        return sum(scores)
    except ValueError:
        return -1


if __name__ == '__main__':
    ops = [5, 2, "C", "D", "+"]
    assert solve_method(ops) == 30

    ops = [5, -2, 4, "C", "D", 9, "+", "+"]
    assert solve_method(ops) == 27

    ops = [1]
    assert solve_method(ops) == 1

    ops = ["+"]
    assert solve_method(ops) == -1
