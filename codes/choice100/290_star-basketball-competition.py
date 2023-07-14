#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 290_star-basketball-competition.py
@time: 2023/7/15 1:07
@project: huawei-od-python
@desc: 290 星际篮球争霸赛
"""


def split_score(arr, num, original_num):
    if len(arr) == 0 and num == original_num:
        return True

    flag = False
    for i in range(len(arr)):
        # 去掉当前得分，继续判断是否还能平分得分
        sub_arr = arr[:i] + arr[i + 1:]
        if arr[i] == num:
            # 示例中等于2的情况
            flag = flag or split_score(sub_arr, original_num, original_num)
        elif arr[i] < num:
            # 示例中等于5的情况
            flag = flag or split_score(sub_arr, num - arr[i], original_num)

    return flag


def solve_method(arr):
    sum_score = sum(arr)
    num = len(arr)
    # 最大可能由num个球员进球，逐步递减，计算最多能被多少个球员平分得分
    for i in range(num, 0, -1):
        if sum_score % i == 0:
            # 判断是否能平分成功
            if split_score(arr, sum_score // i, sum_score // i):
                return sum_score // i

    return sum_score


if __name__ == '__main__':
    assert solve_method([5, 2, 1, 5, 2, 1, 5, 2, 1]) == 6
