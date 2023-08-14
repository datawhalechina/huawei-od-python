#!/usr/bin/env python
# encoding: utf-8
"""
@author: LiYuHong
@file: 161_longest-substring-in-circle.py
@time: 2023/8/8 21:27
@project: huawei-od-python
@desc: 161 环中最长子串
"""


def solve_method(s):
    n = len(s)
    # 统计o的个数，便于计算奇偶性
    cnt = s.count('o')
    # 偶数最长为整个s的长度，奇数则为去掉一个o的长度
    return n - 1 if cnt % 2 else n


if __name__ == '__main__':
    assert solve_method("alolobo") == 6
    assert solve_method("looxdolx") == 7
    assert solve_method("bcbcbc") == 6
    assert solve_method("olo") == 3
