#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 043_max-cards-number.py
@time: 2023/7/27 13:30
@project: huawei-od-python
@desc: 043 卡片组成的最大数字
"""


def solve_method(strings):
    length = len(strings)

    for i in range(length):
        for j in range(i + 1, length):
            if int(strings[i] + strings[j]) < int(strings[j] + strings[i]):
                strings[i], strings[j] = strings[j], strings[i]

    return "".join(strings)


if __name__ == '__main__':
    assert solve_method(["22", "221"]) == "22221"
    assert solve_method(["4589", "101", "41425", "9999"]) == "9999458941425101"
