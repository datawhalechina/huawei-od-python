#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 218_colorize-the-blackboard.py
@time: 2023/7/23 0:50
@project: huawei-od-python
@desc: 218 黑板上色
"""


def solve_method(nums):
    # 去重
    nums = set(nums)
    # 如果有数字1，则只需要一种颜色
    if 1 in nums:
        return 1

    # 重新转换成列表，并排序
    nums = list(nums)
    nums.sort()
    # 遍历数组
    i = 0
    while i < len(nums):
        cur = nums[i]
        j = i + 1
        # 删除数组中能被整除的数
        while j < len(nums):
            if nums[j] % cur == 0:
                nums.pop(j)
            else:
                j += 1
        i += 1

    # 返回剩余数组的长度，即为需要的最少颜色种数
    return len(nums)


if __name__ == '__main__':
    assert solve_method([2, 4, 6]) == 1
    assert solve_method([2, 3, 4, 9]) == 2
