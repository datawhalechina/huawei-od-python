# 064 寻找最大价值的矿堆

## 题目描述

给你一个由0（空地）、1（银矿）、2（金矿）组成的的地图，矿堆只能由上下左右相邻的金矿或银矿连接形成。超出地图范围可以认为是空地。

假设银矿价值1，金矿价值2，请你找出地图中最大价值的矿堆并输出该矿堆的价值。

## 输入描述

地图元素信息如：
```text
22220
00000
00000
11111
```

地图范围最大`300*300`，每个元素的取值范围是0 <= 地图元素 <= 2。

## 输出描述

矿堆的最大价值。

## 示例描述

### 示例一

**输入：**
```text
22220
00000
00000
01111
```

**输出：**
```text
8
```

### 示例二

**输入：**
```text
22220
00020
00010
01111
```

**输出：**
```text
15
```

### 示例三

**输入：**
```text
20000
00020
00000
00111
```

**输出：**
```text
3
```

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 使用深度优先搜索遍历地图上每一个元素：
    - 确定参数：当前行坐标`row`和列坐标`col`。
    - 终止条件：如果超出边界或者已经访问过（标记为-1），则返回0。
    - 递归处理：
        - 将该地图元素设置为已经访问过，标记为-1。
        - 上下左右进行递归搜索，累加所有访问过的矿堆价值。
        - 比较并得到矿堆的最大价值。
2. 返回结果，即矿堆的最大价值。

## 解题代码

```python
def solve_method(nums):
    m, n = len(nums), len(nums[0])
    if m < 1:
        return 0

    def dfs(row, col):
        nonlocal value
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or nums[row][col] == 0 or nums[row][col] == -1:
            # 如果超出边界或者已经访问过（标记为-1），则返回0
            return 0
        else:
            value = nums[row][col]
            # 已经访问过，标记为-1
            nums[row][col] = -1
            for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                # 上下左右进行深度优先搜索
                value += dfs(row + d1, col + d2)
            return value

    max_value = -1
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1 or nums[i][j] == 2:
                value = dfs(i, j)
                if value > max_value:
                    max_value = value
    return max_value


if __name__ == '__main__':
    arr = [[2, 2, 2, 2, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 1, 1, 1, 1]]
    assert solve_method(arr) == 8

    arr = [[2, 2, 2, 2, 0],
           [0, 0, 0, 2, 0],
           [0, 0, 0, 1, 0],
           [0, 1, 1, 1, 1]]
    assert solve_method(arr) == 15
```

