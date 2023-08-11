#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 091_replace-binary-trees-by-path.py
@time: 2023/8/10 18:08
@project: huawei-od-python
@desc: 091 按路径替换二叉树
"""
import itertools


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(nums, index):
    node = None
    if index < len(nums) and nums[index] != 0:
        node = TreeNode(nums[index])
        node.left = build_tree(nums, 2 * index + 1)
        node.right = build_tree(nums, 2 * index + 2)
    return node


def replace_tree(root_tree: TreeNode, sub_tree: TreeNode, path: list, i):
    if i == len(path) - 1:
        if root_tree.left and root_tree.left.val == path[i]:
            root_tree.left = sub_tree
            return
        elif root_tree.right and root_tree.right.val == path[i]:
            root_tree.right = sub_tree
            return

    if root_tree.left and root_tree.left.val == path[i]:
        replace_tree(root_tree.left, sub_tree, path, i + 1)
    elif root_tree.right and root_tree.right.val == path[i]:
        replace_tree(root_tree.right, sub_tree, path, i + 1)


def flatten_tree(node: TreeNode, level: int, node_nums):
    if len(node_nums) == level:
        node_nums.append([])

    node_nums[level].append(node.val)

    if node.left and node.left.val != 0:
        flatten_tree(node.left, level + 1, node_nums)
    if node.right and node.right.val != 0:
        flatten_tree(node.right, level + 1, node_nums)


def solve_method(root_tree_nums, subtree_path, sub_tree_nums):
    subtree_path = subtree_path[1:].split("/")
    subtree_path = [0 if x == "" else int(x) for x in subtree_path]

    # 构建根二叉树和子二叉树
    root_tree = build_tree(root_tree_nums, 0)
    sub_tree = build_tree(sub_tree_nums, 0)

    if len(sub_tree_nums) > 1:
        replace_tree(root_tree, sub_tree, subtree_path, 1)
    else:
        # 子二叉树不存在，根二叉树存在，则取根二叉树的值
        root_tree = sub_tree

    # 展开根二叉树为数组
    result = []
    flatten_tree(root_tree, 0, result)
    return list(itertools.chain(*result))


if __name__ == '__main__':
    root = [1, 1, 2, 0, 0, 4, 5]
    nodes = "/1/2"
    sub_tree = [5, 3, 0]
    assert solve_method(root, nodes, sub_tree) == [1, 1, 5, 3]

    root = [1, 1, 2, 0, 0, 4, 5]
    nodes = "/1/1"
    sub_tree = [5, 3, 0]
    assert solve_method(root, nodes, sub_tree) == [1, 5, 2, 3, 4, 5]
