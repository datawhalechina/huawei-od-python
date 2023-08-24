#!/usr/bin/env python
# encoding: utf-8
"""
@author:  zhangchao
@file: 073_quick-construct-station
@time:  24/8/2023 下午 2:57
@project:  huawei-od-python 
"""


class Node:
    def __init__(self, val, nexts=None, in_=0, out_=0, edges=None):
        self.val = val
        self.nexts = nexts
        self.in_ = in_
        self.out_ = out_
        self.edges = edges


class Edge:
    def __init__(self, from_, to_, weight=None):
        self.from_ = from_
        self.to_ = to_
        self.weight = weight


class Graph:
    def __init__(self, nodes=None, edges=None):
        self.edges = edges
        self.nodes = nodes


def solve_method(num_node, edge_lst):
    graph = Graph(nodes=dict(), edges=set())
    for val in range(num_node):
        graph.nodes[val] = Node(val, nexts=[], edges=[])
    for from_, to_ in edge_lst:
        graph.nodes[from_].nexts.append(to_)
        graph.nodes[to_].in_ += 1
    zeroMap = []
    ans = 0
    while graph.nodes:
        for node in graph.nodes:
            if graph.nodes[node].in_ == 0:
                zeroMap.append(node)
        while zeroMap:
            node = zeroMap.pop()
            for next_node in graph.nodes[node].nexts:
                graph.nodes[next_node].in_ -= 1
            graph.nodes.pop(node)
        ans += 1
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    num_edges = int(input().strip())
    edges = []
    for _ in range(num_edges):
        edges.append(map(int, input().strip().split(' ')))
    res = solve_method(n, edges)
    print(res)
