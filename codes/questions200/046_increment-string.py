#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 046_increment-string.py
@time: 2023/8/22 21:32
@project: huawei-od-python
@desc: 046 递增字符串
"""


def solve_method(chars):
    total_A = chars.count("A")
    res = total_A
    count_A = 0
    for i in range(len(chars)):
        if chars[i] == "A":
            count_A += 1
        # 将区间[0, i]全部转成A的修改次数
        count_before_i = i + 1 - count_A
        # 将区间[i+1, len(chars)]全部转为B的修改次数
        count_after_i = total_A - count_A
        # 计算最小值
        res = min(res, count_before_i + count_after_i)
    return res


if __name__ == "__main__":
    # AABBA
    # str = input().strip()
    # print(solve_method(str))

    assert solve_method("AABBA") == 1
    assert solve_method("BAABBABBAB") == 3
