#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 066_find-path
@time:  2023/8/14 14:51
@project:  huawei-od-python
@desc: 066 寻找路径
"""
import math


def solve_method(nums):
    nums.insert(0, 0)
    # nums第一个元素无意义，为额外添加元素，目的是对齐下标
    depth = math.ceil(math.log2(len(nums)))
    # 得到最后一层节点的索引
    start = 2 ** (depth - 1)
    min_value, index = math.inf, -1
    # 遍历该层的所有节点
    for i in range(start, len(nums)):
        if nums[i] != -1 and nums[i] < min_value:
            # 取出最小的叶子节点
            min_value, index = nums[i], i
    # 得到该节点的路径
    path = []
    while index > 0:
        path.append(nums[index])
        index = index // 2
    return path[::-1]


if __name__ == '__main__':
    tree_nodes = [3, 5, 7, -1, -1, 2, 4]
    assert solve_method(tree_nodes) == [3, 7, 2]

    tree_nodes = [5, 9, 8, -1, -1, 7, -1, -1, -1, -1, -1, 6]
    assert solve_method(tree_nodes) == [5, 8, 7, 6]
