#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 076_discount-fruit
@time:  2023/7/30 22:41
@project:  huawei-od-python
@desc: 076 打折买水果
"""


def solve_method(m, n, price):
    '''
    m:水果超市个数
    n:小时数
    :param m:
    :param n:
    :param price:
    :return:
    '''
    price = sorted(price, key=lambda x: x[2])
    cost = 0
    for i in range(n):
        for j in range(m):
            if price[j][0] <= i + 1 <= price[j][1]:
                cost += price[j][2]
                break
    return cost


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    price = [list(map(int, input().strip(' '))) for _ in range(m)]
    res = solve_method(m, n, price)
    print(res)
