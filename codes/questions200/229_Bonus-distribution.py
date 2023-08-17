#!/usr/bin/env python
# encoding: utf-8
"""
@author: ZhouLixuan
@file: 229_Bonus-distribution.py
@time: 2023/8/14
@project: huawei-od-python
@desc: 229 分奖金
"""

def solve_method(rand_numbers):
    res = []

    for i in range(len(rand_numbers)):
        num = rand_numbers[i]
        find = False
        # 往后找大于 该员工 随机数 的值
        for j in range(i, len(rand_numbers)):
            other = rand_numbers[j]
            if other > num:
                # 奖金 = 第一个比该员工随机数大的数字到随机数的距离 * 数字差值
                res.append((j - i) * (other - num))
                find = True
                break
        if not find:
            # 找不到更大的随机数，奖金 = 该员工的的随机数字
            res.append(num)

    return res

if __name__ == '__main__':
    rand_numbers = [2, 10, 3]
    assert solve_method(rand_numbers) == [8, 10, 3]