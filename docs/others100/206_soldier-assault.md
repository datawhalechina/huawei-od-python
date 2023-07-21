# 206 速战速决、士兵突击

## 题目描述

在一个`M * N`的街区中，有一个士兵`S`和一个敌人`E`，标识`X`为无法通过的街区，标识`B`为可以通过的街区。士兵在一个单位时间内可以从一个街区移动到相邻的街区（士兵每次只能水平或者垂直方向移动一个街区）。士兵每次改变方向时，需要额外花费1个单位的时间（士兵第1次移动到街区的时候，不用考虑其初始方向，即只需要一个单位时间即可达到相邻街区）。

计算士兵`S`最少需要多少时间才能到达`E`所在的街区。

## 输入描述

第1行为两个数字，表示街区的大小，大小为`M`行`N`列。其中，`1 <= M * N <= 1000`，`M`、`N`不同时为1。

接下来`M`行，每行`N`个字母，字母`S`表示士兵所在街区，字母`E`表示敌人所在街区，字母`X`表示障碍，字母`B`表示可以经过的街区。（只有1个`S`和1个`E`）

## 输出描述

最少需要的时间，当士兵`S`永远无法达到敌人`E`所在的街区时，输出-1。

## 示例描述

### 示例一

**输入：**
```text
6 6
SBBBBB
BXXXXB
BBXBBB
XBBXXB
BXBBXB
BBXBEB
```

**输出：**
```text
13
```

## 解题思路

**基本思路：** 使用深度优先搜索DFS进行解题。
1. 遍历街区列表，得到起始坐标、终点坐标
2. 深度优先搜索：
   - 确定参数：坐标`(x, y)`、所需步数`length`、方向`direction_index`、路径`path`、最少需要的步数`result`
   - 固定参数：终点坐标`(end_x, end_y)`、街区列表`block`、街区大小`M`行`N`列。
   - 终止条件：当达到了终点坐标，比较所需步数，取最小值。
   - 递归过程：在四个方向上进行深度优先搜索，士兵每次改变方向时，需要额外花费1个单位的时间。
3. 返回最少需要的步数。

## 解题代码

```python
import math


def dfs(x, y, length, direction_index, end_x, end_y, M, N, block, paths, result):
    if x == end_x and y == end_y:
        result = min(result, length)
        return result

    paths.append((x, y))
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    # 各个方向上深度优先搜索
    for i in range(4):
        new_x, new_y = x + directions[i][0], y + directions[i][1]
        if (new_x < 0 or
                new_y < 0 or
                new_x >= M or
                new_y >= N or
                block[new_x][new_y] == "X" or
                (new_x, new_y) in paths):
            continue

        # 士兵每次改变方向时，需要额外花费1个单位的时间
        result = dfs(new_x, new_y, length + int(i != direction_index) + 1, i, end_x, end_y, M, N, block, paths, result)

    return result


def solve_method(block):
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for row in range(len(block)):
        for col in range(len(block[0])):
            # 得到起始坐标
            if block[row][col] == "S":
                start_x, start_y = row, col
            # 得到终点坐标
            if block[row][col] == "E":
                end_x, end_y = row, col
    paths = []
    result = math.inf
    M = len(block)
    N = len(block[0])

    result = dfs(start_x, start_y, -1, -1, end_x, end_y, M, N, block, paths, result)

    return result


if __name__ == '__main__':
    block = ["SBBBBB",
             "BXXXXB",
             "BBXBBB",
             "XBBXXB",
             "BXBBXB",
             "BBXBEB"]
    assert solve_method(block) == 13
```