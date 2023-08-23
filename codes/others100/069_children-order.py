#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 069_children-order
@time:  23/8/2023 下午 7:19
@project:  huawei-od-python 
"""


def solve_method(line):
    nums = line.strip().split(' ')
    try:
        nums = list(map(int, nums))
    except:
        return '[]'
    for i in range(len(nums) - 1):
        if i & 1 == 1 and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        elif i & 1 == 0 and nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return ' '.join(nums)


if __name__ == '__main__':
    line = input()
    res = solve_method(line)
    print(res)
