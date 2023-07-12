# 271 基站维修工程师

## 题目描述

小王是一名基站维护工程师，负责某区域的基站维护。某地方有`n`个基站（`1 < n < 10`），已知各基站之间的距离`s`（`0 < s < 500`），并且基站`x`到基站`y`的距离，与基站`y`到基站`x`的距离并不一定会相同。

小王从基站1出发，途径每个基站1次，然后返回基站1，需要请你为他选择一条距离最短的路径。

## 输入描述

第一行表示站点数，以后各行表示站点数`n`到各站点之间的距离（均为整数）。
```
3
0 2 1
1 0 2
2 1 0
```

## 输出描述

最短路径的数值。

## 示例描述

### 示例一

**输入：**
```
3
0 2 1
1 0 2
2 1 0
```

**输出：**
```
3
```

## 解题思路

1. 本题采用可放回的回溯法。
2. 由于固定从基站1开始，可设置初始路径列表为`[0]`，路径长度和路径节点一致，使用回溯法得到所有可能的路径。
3. 根据得到的路径，计算路径长度，得到最小路径。

## 解题代码

```python
import math


def solve_method(num, paths):
    result = []
    backstracking(num, num, 1, [0], result)

    min_path = math.inf
    for path in result:
        total_path = 0
        prev = 0
        for p in path:
            # 计算路径长度
            total_path += paths[prev][p]
            prev = p

        if total_path < min_path:
            min_path = total_path
    return min_path


def backstracking(n, k, start_index, path, result):
    if len(path) == k:
        tmp = path[:]
        tmp.append(0)
        result.append(tmp)
        return

    # 采用放回的取数方式
    for i in set(range(n)).difference(set(path)):
        path.append(i)
        backstracking(n, k, i + 1, path, result)
        path.pop()
```