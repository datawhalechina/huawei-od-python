#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: 034_remove-a-specified-directory.py
@time: 2023/8/8 9:06
@project: huawei-od-python
@desc: 034 删除指定目录
"""
from collections import defaultdict


def build_tree(dirs, tree):
    for dir_ids in dirs:
        node, parent = dir_ids[0], dir_ids[1]
        tree[parent].append(node)


def rm_node(tree, node):
    # 删除子目录
    for k, v in tree.items():
        if node in v:
            v.remove(node)

    if node in tree.keys():
        # 删除父目录
        children = tree.pop(node)

        for sub_node in children:
            # 递归删除目录
            rm_node(tree, sub_node)


def solve_method(dirs, dir_id):
    tree = defaultdict(list)
    build_tree(dirs, tree)
    rm_node(tree, dir_id)

    result = set()
    for k, v in tree.items():
        if k != 0:
            result.add(k)
            for node in v:
                result.add(node)
    return list(sorted(result))


if __name__ == '__main__':
    dirs = [[8, 6],
            [10, 8],
            [6, 0],
            [20, 8],
            [2, 6]]
    assert solve_method(dirs, 8) == [2, 6]
