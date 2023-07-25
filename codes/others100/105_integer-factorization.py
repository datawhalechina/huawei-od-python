#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 105_integer-factorization.py
@time: 2023/7/25 22:06
@project: huawei-od-python
@desc: 105 整数分解
"""
import math


def solve_method_1(t):
    result = []
    result.append("{}={}".format(t, t))
    count = 1
    # 对整数的一半向上取整 因为后面的数没有可能是答案
    for i in range(math.ceil(t / 2) - 1, 0, -1):
        sum_num = i
        expression = "{}={}".format(t, i)
        for j in range(i + 1, math.ceil(t / 2) + 1):
            sum_num += j
            expression = expression + "+" + str(j)
            if sum_num == t:
                result.append(expression)
                count += 1
                break

    result.append("Result:{}".format(count))
    return result


def solve_method_2(t):
    result = []
    result.append("{}={}".format(t, t))
    count = 1
    # 对整数的一半向上取整 因为后面的数没有可能是答案
    for i in range(math.ceil(t / 2) - 1, 0, -1):
        # 利用等差数数列公式求解，应为m要求大于零所以排除一个解
        m = ((8 * t + (2 * i - 1) ** 2) ** .5 - 2 * i + 1) / 2
        if m.is_integer():
            count += 1
            result.append("{}={}".format(t, "+".join(map(str, range(i, i + int(m))))))
    result.append("Result:{}".format(count))
    return result


if __name__ == "__main__":
    solve_methods = [solve_method_1, solve_method_2]
    for solve_method in solve_methods:
        assert solve_method(9) == ["9=9", "9=4+5", "9=2+3+4", "Result:3"]
        assert solve_method(10) == ["10=10", "10=1+2+3+4", "Result:2"]
