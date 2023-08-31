#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 011_bonus-distribution.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 011 分奖金
"""


def solve_method(rand_numbers):
    res = []

    for i in range(len(rand_numbers)):
        num = rand_numbers[i]
        find = False
        # 往后找大于该员工随机数的值
        for j in range(i, len(rand_numbers)):
            other = rand_numbers[j]
            if other > num:
                # 如果遇到第一个比自己数字大的，则奖金等于距离*数字差值，并跳出循环
                res.append((j - i) * (other - num))
                find = True
                break
        if not find:
            # 如果找不到更大的随机数，则奖金等于该员工的随机数值
            res.append(num)

    return res


if __name__ == '__main__':
    rand_numbers = [2, 10, 3]
    assert solve_method(rand_numbers) == [8, 10, 3]
