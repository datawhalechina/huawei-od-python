#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 214_non-strictly-increment-sequence.py
@time: 2023/7/22 22:45
@project: huawei-od-python
@desc: 214 非严格递增连续数字序列
"""
import math


def solve_method(string):
    # 设置前一个数字
    pre_num = math.inf
    # 满足条件的最大长度
    max_len = 0
    cur_len = 0
    for ch in string:
        if ch.isdigit():
            ch = int(ch)
            # 如果当前数字大于等于前一个数字，则继续保持非严格递增
            if cur_len == 0 or ch >= pre_num:
                cur_len += 1
            else:
                # 如果没有，则长度回到1
                max_len = max(max_len, cur_len)
                cur_len = 1
            # 保存前一个数字
            pre_num = ch
        else:
            # 如果不是数字，则直接保存当前长度
            max_len = max(max_len, cur_len)
            cur_len = 0
            pre_num = math.inf

    return max(cur_len, max_len)


if __name__ == '__main__':
    assert solve_method("abc2234019A334bc") == 4
