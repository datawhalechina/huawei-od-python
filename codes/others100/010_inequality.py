#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 010_inequality.py
@time: 2023/7/26 16:24
@project: huawei-od-python
@desc: 010 不等式
"""


def check_and_calc(value, b, sign):
    if sign == ">":
        return value > b
    elif sign == "<":
        return value < b
    elif sign == ">=":
        return value >= b
    elif sign == "<=":
        return value <= b
    elif sign == "=":
        return value == b


def solve_method(A, X, B, signs):
    result = []
    right = True
    for a, b, sign in zip(A, B, signs):
        # 计算左侧value值
        value = 0
        for i in range(len(a)):
            value += a[i] * X[i]

        # 计算误差
        e = int(abs(value - b))
        # 验证不等式是否成立
        right = check_and_calc(value, b, sign) and right
        # 存储误差
        result.append(e)

    return "true" if right else "false", max(result)


if __name__ == '__main__':
    A = [[2.3, 3, 5.6, 7, 6],
         [11, 3, 8.6, 25, 1],
         [0.3, 9, 5.3, 66, 7.8]]
    X = [1, 3, 2, 7, 5]
    B = [340, 670, 80.6]
    sign = ["<=", "<=", "<="]
    assert solve_method(A, X, B, sign) == ("false", 458)

    A = [[2.36, 3, 6, 7.1, 6],
         [1, 30, 8.6, 2.5, 21],
         [0.3, 69, 5.3, 6.6, 7.8]]
    X = [1, 13, 2, 17, 5]
    B = [340, 67, 300.6]
    sign = ["<=", "<=", "<="]
    assert solve_method(A, X, B, sign) == ("false", 758)
