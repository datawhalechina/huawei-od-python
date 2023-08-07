#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 030_sharing-blocks.py
@time: 2023/8/7 20:58
@project: huawei-od-python
@desc: 030 分积木
"""


def solve_method(blocks):
    count = 0
    for i in blocks:
        # 进行异或运算，等同于不进位的加法
        count = count ^ i
    if count == 0:
        return sum(blocks) - min(blocks)
    else:
        return "No"


if __name__ == '__main__':
    assert solve_method([3, 5, 6]) == 11
