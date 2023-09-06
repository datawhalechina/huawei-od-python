# 141 树状结构查询

## 题目描述

通常使用多行的节点、父节点表示一棵树，比如：
```text
西安 陕西
陕西 中国
江西 中国
中国 亚洲
泰国 亚洲
```

输入一个节点之后，请打印出来树中该节点的所有下层节点。

## 输入描述

第一行输入行数。

下面是多行数据，每行以空格区分节点和父节点。

接着是查询节点。

## 输出描述

输出查询节点的所有下层节点。以字典序排序。

**补充说明：**

树中的节点是唯一的，不会出现两个节点，是同一个名字。

## 示例描述

### 示例一

**输入：**
```text
5
b a
c a
d c
e c
f d
c
```

**输出：**
```text
d
e
f
```

## 解题思路

**基本思路：** 使用广度优先搜索BFS求解。
1. 初始化父节点下的所有子节点字典`nodes`，`key`为父节点，`value`为所有子节点。
2. 得到目标节点的所有子节点`children`。
3. 使用广度优先搜索，遍历所有子节点：
   - 取出第一个子节点，并加入到结果列表中
   - 找到该子节点对应的所有子节点，加入到待遍历列表中。
   - 当所有待遍历列表中的子节点都已访问过，则跳出遍历。
4. 对结果列表按照字典序排序。
5. 返回结果列表。

## 解题代码
```python
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
```