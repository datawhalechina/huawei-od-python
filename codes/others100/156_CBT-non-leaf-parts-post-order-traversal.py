#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 156_CBT-non-leaf-parts-post-order-traversal.py
@time: 2023/9/3 3:59
@project: huawei-od-python
@desc: 002 完全二叉树非叶子部分后序遍历
"""


def solve_method(nums):
    def post_order_non_leaf(index):
        # 如果索引超出列表范围，返回空列表
        if index >= len(nums):
            return []

        # 计算左右子节点的索引
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # 后序遍历：先左子树，再右子树，最后根节点
        left_result = post_order_non_leaf(left_child)
        right_result = post_order_non_leaf(right_child)

        # 如果当前节点是非叶子节点，添加到结果中
        if left_child < len(nums) or right_child < len(nums):
            return left_result + right_result + [index]
        return []

    non_leaf_index = post_order_non_leaf(0)
    return [nums[x] for x in non_leaf_index]


if __name__ == "__main__":
    assert solve_method([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 1]
    assert solve_method([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 5, 2, 3, 1]
