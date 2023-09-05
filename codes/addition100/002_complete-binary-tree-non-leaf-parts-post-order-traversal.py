#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 002_complete-binary-tree-non-leaf-parts-post-order-traversal.py
@time: 2023/9/3 3:59
@project: huawei-od-python
@desc: 
"""


def post_order_non_leaf(ints, index):
    """后序遍历完全二叉树并返回非叶子节点的索引。"""

    # 如果索引超出列表范围，返回空列表
    if index >= len(ints):
        return []

    # 计算左右子节点的索引
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # 后序遍历：先左子树，再右子树，最后根节点
    left_result = post_order_non_leaf(ints, left_child)
    right_result = post_order_non_leaf(ints, right_child)

    # 如果当前节点是非叶子节点，添加到结果中
    if left_child < len(ints) or right_child < len(ints):
        return left_result + right_result + [index]
    return []


def main():
    """主函数：从用户那里读取输入，执行后序遍历，并打印非叶子节点的值。"""

    # 读取并转换输入
    ints = list(map(int, input("Enter the integers separated by spaces:").split()))

    # 获取非叶子节点的索引
    non_leaf_index = post_order_non_leaf(ints, 0)

    # 打印非叶子节点的值
    print("".join(str(ints[i]) for i in non_leaf_index))


# 如果此脚本作为主程序运行，则执行main函数
if __name__ == "__main__":
    main()

