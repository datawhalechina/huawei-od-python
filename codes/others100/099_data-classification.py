#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 099_data-classification.py
@time: 2023/8/11 21:36
@project: huawei-od-python
@desc: 099 数据分类
"""
from collections import defaultdict


def solve_method(c, b, nums):
    result = defaultdict(int)

    for num in nums:
        # 转成16进制
        hex_num = str(hex(num))
        # 转成4字节，位数不够，填充0
        hex_num = hex_num[2:].zfill(8)
        sum_ = 0
        for i in range(0, 8, 2):
            sum_ += int(hex_num[i: i + 2], 16)

        if sum_ % b < c:
            # 统计有效类型的个数
            result[sum_ % b] += 1

    # 返回类型最多的个数
    return max(result.values())


if __name__ == '__main__':
    nums = [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]
    assert solve_method(3, 4, nums) == 3

    nums = [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]
    assert solve_method(1, 4, nums) == 2
