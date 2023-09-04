# 048 可以组成网络的服务器

## 题目描述

在一个机房中，服务器的位置标识在`n*m`的整数矩阵网格中，1表示单元格上有服务器，0表示没有。如果两台服务器位于同一行或者同一列中紧邻的位置，则认为它们之间可以组成一个局域网。请你统计机房中最大的局域网包含的服务器个数。

## 输入描述

第一行输入两个正整数，`n`和`m`，取值范围是0 < n,m <= 100。

之后为`n*m`的二维数组，代表服务器信息。

## 输出描述

最大局域网包含的服务器个数。

## 示例描述

### 示例一

**输入：**
```text
2 2
1 0
1 1
```

**输出：**
```text
3
```

**说明：**  

`[0][0],[1][0],[1][1]`三台服务器相互连接，可以组成局域网。

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 使用深度优先搜索，遍历矩阵中的每一个元素：
    - 确定参数：元素的坐标`i`和`j`，联通的服务器个数`count`。
    - 终止条件：如果超出边界，或者该位置为0，则返回服务器个数。
    - 递归处理：向上下左右四个方向递归搜索，并累加连通区域的大小。
2. 更新最大的连通区域的大小，并返回结果。    

## 解题代码
```python
def solve_method(n, m, servers):
    def dfs(i, j, count):
        if i < 0 or i >= n or j < 0 or j >= m or servers[i][j] == 0:
            return count
        count += 1
        # 避免重复计算
        servers[i][j] = 0
        count = dfs(i + 1, j, count)
        count = dfs(i - 1, j, count)
        count = dfs(i, j + 1, count)
        count = dfs(i, j - 1, count)
        return count
    
    max_count = 0
    for i in range(n):
        for j in range(m):
            max_count = max(max_count, dfs(i, j, 0))
    return max_count


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # servers = []
    # for _ in range(n):
    #     servers.append(list(map(int, input().split())))

    servers = [[1, 0],
               [1, 1]]
    assert solve_method(2, 2, servers) == 3

    servers = [[1, 0, 0],
               [1, 0, 1],
               [0, 1, 1]]
    assert solve_method(3, 3, servers) == 3
```