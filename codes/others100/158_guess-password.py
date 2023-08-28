#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 158_guess-password.py
@time: 2023/8/29 0:20
@project: huawei-od-python
@desc: 158 猜密码
"""

from itertools import combinations


def get_possible_combinations(digits, min_length):
    # 生成所有可能的组合
    combinations_list = []
    for length in range(min_length, len(digits) + 1):
        combinations_list.extend(combinations(digits, length))

    # 按照要求进行排序
    combinations_list.sort(key=lambda x: (len(x), x))

    return combinations_list


# 读取输入
digits = input().split(",")
min_length = int(input())

# 调用函数获取可能的密码组合
combinations_list = get_possible_combinations(digits, min_length)

# 输出结果
if combinations_list:
    for combination in combinations_list:
        print("".join(combination))
else:
    print("None")
