# 073 快速开租建站

## 题目描述

当前IT部门支撑了子公司颗粒化业务，
该部门需要实现为子公司快速开租建站的能力，
建站是指在一个全新的环境部署一套IT服务。
每个站点开站会由一系列部署任务项构成，
每个任务项部署完成时间都是固定和相等的，设为1。
部署任务项之间可能存在依赖，假如任务2依赖任务1，
那么等任务1部署完，任务2才能部署。
任务有多个依赖任务则需要等所有依赖任务都部署完该任务才能部署。
没有依赖的任务可以并行部署，优秀的员工们会做到完全并行无等待的部署。
给定一个站点部署任务项和它们之间的依赖关系，请给出一个站点的最短开站时间。
## 输入描述
第一行是任务数taskNum，第二行是任务的依赖关系数relationsNum。
接下来relationsNum行，每行包含两个id，描述一个依赖关系，格式为:IDi IDj，
表示部署任务i部署完成了，部署任务j才能部署，IDi和IDj值的范围为:[0, taskNum)

注:输入保证部署任务之间的依赖不会存在环。




## 输出描述
一个整数,表示一个站点的最短开站时间。

**备注：**

1 < taskNum <=100

1 <= relationsNum <= 5000

## 示例描述

### 示例一

**输入：**
```text
5
5
0 4
1 2
1 3
2 3
2 4
```

**输出：**
```text
3
```

**说明：**

有5个部署任务项，5个依赖关系。
我们可以先同时部署任务项0和任务项1，然后部署任务项2，最后同时部署任务项3和任务项4。最短开站时间为3。

### 示例二

**输入：**
```text
5
3
0 3
0 4
1 3
```

**输出：**
```text
2
```
**说明：**

有5个部署任务项，3个依赖关系。我们可以先同时部署任务项0，任务项1，任务项2。
然后再同时部署任务项3和任务项4。最短开站时间为2。

## 解题思路
拓扑排序，每次剔除入度为0的节点，同时更新节点入度，直到所有节点入度为0
## 解题代码

```python
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

```

