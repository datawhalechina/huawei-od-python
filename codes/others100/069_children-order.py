#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 069_children-order
@time:  2023/8/23 19:19
@project:  huawei-od-python
@desc: 069 小朋友排队
"""


def solve_method(nums):
    # 检查参数是否合法
    if all([False if str(x).isdigit() else True for x in nums]):
        return []

    for i in range(len(nums) - 1):
        if i & 1 == 1 and nums[i] > nums[i + 1]:
            # 当索引为奇数时，如果当前的小朋友身高比后一个小朋友的身高要高，则需要交换
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        elif i & 1 == 0 and nums[i] < nums[i + 1]:
            # 当索引为偶数时，0也算作偶数，如果当前的小朋友身高比后一个小朋友的身高要矮，则需要交换
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


if __name__ == '__main__':
    assert solve_method([4, 1, 3, 5, 2]) == [4, 1, 5, 2, 3]
    assert solve_method([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert solve_method(["xxx"]) == []
