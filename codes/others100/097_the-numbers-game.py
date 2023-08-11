#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 097_the-numbers-game.py
@time: 2023/8/11 20:51
@project: huawei-od-python
@desc: 097 数字游戏
"""


def solve_method(cases):
    result = []
    for case in cases:
        m = case[0]
        pokers = case[1]

        # 累加和
        pre_sum = 0
        is_true = 0
        # 余数集合
        remainders = set()
        for poker in pokers:
            pre_sum = (pre_sum + poker) % m
            # 如果余数与前几次的余数相同，则表示其中一定存在连续累加为m的数字
            if pre_sum in remainders:
                is_true = 1
                break
            remainders.add(pre_sum)

        result.append(is_true)

    return result


if __name__ == '__main__':
    cases = [[7, [4, 4, 2, 5, 3, 5, 5]],
             [11, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]
    assert solve_method(cases) == [1, 0]
