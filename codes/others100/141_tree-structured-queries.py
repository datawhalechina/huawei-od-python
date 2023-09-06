#!/usr/bin/env python
# encoding: utf-8
"""
@author: Kaiwen Zuo
@file: 141_tree-structured-queries.py
@time: 2023/9/2 4:42
@project: huawei-od-python
@desc: 001 树状结构查询
"""
from collections import defaultdict


def solve_method(tree, target):
    # 父节点下的所有子节点字典，key为父节点，value为所有子节点
    nodes = defaultdict(list)
    for node in tree:
        nodes[node[1]].append(node[0])

    # 检索目标节点的子节点
    children = nodes.get(target, [])
    result = []

    # 使用广度优先搜索
    while children:
        node = children.pop(0)
        result.append(node)
        children.extend(nodes.get(node, []))

    # 对结果列表按照字典序排序
    result.sort()
    return result


if __name__ == "__main__":
    tree = [["b", "a"], ["c", "a"], ["d", "c"], ["e", "c"], ["f", "d"]]
    assert solve_method(tree, "c") == ["d", "e", "f"]
