#!/usr/bin/env python
# encoding: utf-8
"""
@author: catcooc
@file: 111_new-job-number-system.py
@time: 2023-07-28 11:33:18
@project: huawei-od-python
@desc: 111 新工号系统
"""

import math


def solve_method(x, y):
    # 计算由y个字母能组成的工号个数
    cb = math.pow(26, y)
    result = 1
    if x > cb:
        # 取10为底的log，计算由多少个十数字组成工号。
        result = math.ceil(math.log(x / cb, 10))
    return result


if __name__ == "__main__":
    assert solve_method(260, 1) == 1
    assert solve_method(26, 1) == 1
    assert solve_method(2600, 1) == 2
    assert solve_method(27, 1) == 1
    assert solve_method(2601, 1) == 3
