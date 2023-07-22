#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 210_Alibaba-looks-for-gold-treasure-chests-4.py
@time: 2023/7/22 1:08
@project: huawei-od-python
@desc: 210 阿里巴巴找黄金宝箱（4）
"""


def solve_method(nums):
    res = [0] * len(nums)
    # 当前的遍历位置
    index = 0
    for i in range(len(nums)):
        num = nums[i]
        # j为内部遍历的位置
        j = index + 1
        # 当j达到了最后一个位置，重新回到开始位置
        if j == len(nums):
            j = 0
        while index != j:
            # 如果没有循环一圈
            if num < nums[j]:
                #
                res[i] = nums[j]
                # 保存当前遍历的位置
                index = j
                break
            # 继续遍历
            j += 1
            # 当j达到了最后一个位置，重新回到开始位置
            if j == len(nums):
                j = 0
        # 如果循环一圈都没有找到比当前数大的值，输出-1
        if res[i] == 0:
            res[i] = -1
            # 记录下一个位置
            index = i + 1

    return res


if __name__ == '__main__':
    assert solve_method([1, 2, 3, 6, 3]) == [2, 3, 6, -1, 6]
    assert solve_method([2, 5, 2]) == [5, -1, 5]
    assert solve_method([3, 4, 5, 6, 3]) == [4, 5, 6, -1, 4]
