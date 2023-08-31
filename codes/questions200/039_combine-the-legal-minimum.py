#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 039_combine-the-legal-minimum.py
@time: 2023/8/22 9:50
@project: huawei-od-python
@desc: 039 组合出合法最小数
"""


def solve_method(nums):
    nums_zero, nums_non_zero = [], []
    for num in nums:
        if num.startswith('0'):
            nums_zero.append(num)
        else:
            nums_non_zero.append(num)

    nums_zero.sort()
    nums_non_zero.sort()

    # 如果不存在0开头的数字
    if len(nums_zero) == 0:
        return "".join(nums_non_zero)
    # 如果存在0开头的数字，也存在非0开头的数字
    if len(nums_non_zero) > 0:
        return "".join([nums_non_zero[0]] + nums_zero + nums_non_zero[1:])
    # 如果只存在0开头的数字
    return "".join(nums_zero).lstrip('0')


if __name__ == "__main__":
    # 20 1
    # nums = list(map(str, input().strip().split()))
    # print(solve_method(nums))

    assert solve_method(["20", "1"]) == "120"
    assert solve_method(["08", "10", "2"]) == "10082"
    assert solve_method(["01", "02"]) == "102"
