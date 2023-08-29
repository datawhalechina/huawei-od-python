#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 073_quick-construct-station
@time:  2023/8/24 14:57
@project:  huawei-od-python
@desc: 073 快速开租建站
"""


class Node:
    def __init__(self, val, nexts=None, in_=0, out_=0, edges=None):
        self.val = val
        self.nexts = nexts
        self.in_ = in_
        self.out_ = out_
        self.edges = edges


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes


def solve_method(num_node, edge_lst):
    # 构建图
    graph = Graph(nodes=dict())
    # 初始化节点的值
    for val in range(num_node):
        graph.nodes[val] = Node(val, nexts=[], edges=[])
    # 初始化节点的入度和出度
    for from_, to_ in edge_lst:
        graph.nodes[from_].nexts.append(to_)
        graph.nodes[to_].in_ += 1

    zeroMap = []
    count = 0
    while graph.nodes:
        # 把入度为0的节点，加入到节点列表中
        for node in graph.nodes:
            if graph.nodes[node].in_ == 0:
                zeroMap.append(node)
        # 遍历所有入度为0的节点，并把相关联节点的入度减1
        while zeroMap:
            node = zeroMap.pop()
            for next_node in graph.nodes[node].nexts:
                graph.nodes[next_node].in_ -= 1
            graph.nodes.pop(node)
        count += 1
    return count


if __name__ == '__main__':
    taskNum = 5
    relations = [[0, 4],
                 [1, 2],
                 [1, 3],
                 [2, 3],
                 [2, 4]]
    assert solve_method(taskNum, relations) == 3

    taskNum = 5
    relations = [[0, 3],
                 [0, 4],
                 [1, 3]]
    assert solve_method(taskNum, relations) == 2
