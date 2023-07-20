#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 202_continuous-substrings.py
@time: 2023/7/20 13:47
@project: huawei-od-python
@desc: 202 连续子串
"""


def solve_method(t, p):
    # 实现 t.find(p) + 1
    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        substring = t[i:i + p_len]
        if substring == p:
            return i + 1

    return "No"


if __name__ == '__main__':
    assert solve_method("AVERDXIVYERDIAN", "RDXI") == 4
