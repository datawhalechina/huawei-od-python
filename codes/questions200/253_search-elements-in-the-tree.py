#!/usr/bin/env python
# encoding: utf-8
"""
@author: Libihan
@file: 253_search-elements-in-the-tree.py
@time: 2023/8/21 19:19
@project: huawei-od-python
@desc: 253 查找树中的元素、查找二叉树节点
"""


def solve_method(nodes, pos):
    # 得到满足层数要求的所有节点，节点的索引即为其偏移
    x, y = pos
    res = []
    get_nodes_by_depth(nodes, 0, x, res)
    # 得到满足偏移的节点
    if y > len(res):
        return "{}"
    return "{" + str(res[y]) + "}"


def get_nodes_by_depth(nodes, index, depth, res):
    # 索引index处的节点，node的取值为{节点值，子节点索引1,...}
    node = nodes[index]
    if depth == 0:
        res.append(node[0])
        return res
    # 到达叶子节点
    if len(node) == 1:
        return res
    for i in node[1:]:
        get_nodes_by_depth(nodes, i, depth - 1, res)


if __name__ == "__main__":
    # num = int(input().strip())
    # nodes = []
    # for _ in range(num):
    #     nodes.append(list(map(int, input().strip().split())))
    # x, y = map(int, input().strip().split())
    # print(solve_method(nodes, x, y))

    arr = [[10, 1, 2],
           [-21, 3, 4],
           [23, 5],
           [14],
           [35],
           [66]]
    assert solve_method(arr, (1, 1)) == "{23}"

    arr = [[0, 1, 2, 3, 4],
           [-11, 5, 6, 7, 8],
           [113, 9, 10, 11],
           [24, 12],
           [35],
           [66, 13],
           [77],
           [88],
           [99],
           [101],
           [102],
           [103],
           [25],
           [104]]
    assert solve_method(arr, (2, 5)) == "{102}"
