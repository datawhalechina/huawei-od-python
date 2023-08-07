#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 031_sharing-candies.py
@time: 2023/8/7 21:40
@project: huawei-od-python
@desc: 031 分糖果
"""


def divide_candies(candies_num):
    if candies_num == 2:
        # 当糖果数为2时，返回1
        return 1
    if candies_num % 2 == 0:
        # 当糖果数为偶数时，平均分配
        return divide_candies(candies_num // 2) + 1
    else:
        # 当糖果数为奇数时，取出或放回的次数最小值
        return min(divide_candies(candies_num + 1) + 1, divide_candies(candies_num - 1) + 1)


def solve_method(n):
    if n > 1000000:
        return False

    return divide_candies(n)


if __name__ == '__main__':
    assert solve_method(15) == 5
