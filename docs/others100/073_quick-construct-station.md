# 073 快速开租建站

## 题目描述

当前IT部门支撑了子公司颗粒化业务，该部门需要实现为子公司快速开租建站的能力，建站是指在一个全新的环境部署一套IT服务。

每个站点开站由一系列部署任务项构成，每个任务项部署完成时间都是固定和相等的，设为1。部署任务项之间可能存在依赖，假如任务2依赖任务1，那么等任务1部署完，任务2才能部署。任务有多个依赖任务，则需要等所有依赖任务都部署完该任务才能部署。没有依赖的任务可以并行部署，优秀的员工们会做到完全并行无等待的部署。

给定一个站点部署任务项和它们之间的依赖关系，请给出一个站点的最短开站时间。

## 输入描述

第一行是任务数`taskNum`，取值范围是1 < taskNum <= 100。

第二行是任务的依赖关系数`relationsNum`，取值范围是1 <= relationsNum <= 5000。

接下来`relationsNum`行，每行包含两个`id`，描述一个依赖关系，格式为`IDi IDj`，表示部署任务`i`部署完成，部署任务`j`才能部署，`IDi`和`IDj`的取值范围是`[0, taskNum)`。

注：输入保证部署任务之间的依赖不会存在环。

## 输出描述

输出一个整数，表示一个站点的最短开站时间。

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

有5个部署任务项，3个依赖关系。

我们可以先同时部署任务项0、任务项1、任务项2。然后再同时部署任务项3和任务项4。最短开站时间为2。

## 解题思路

1. 构建图。
2. 初始化图中节点（任务项）的值。
3. 初始化途中节点的入度和出度。
4. 遍历图中左右的节点：
    - 把入度为0的节点，加入到节点列表中。
    - 遍历所有入度为0的节点，并把相关联节点的入度减1。
    - 计数器累加1。
5. 返回计数器的值，即部署次数。    

## 解题代码

```python
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
```

