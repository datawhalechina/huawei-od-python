# 183 聚餐地点、快乐的周末

## 题目描述

小华和小为是很好的朋友，他们约定周末一起吃饭，通过手机交流，他们在地图上选择了很多聚餐地点（由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能达到的聚餐地点有多少个。

## 输入描述

第一行输入`m`和`n`，`m`表示地图长度，`n`表示地图宽度。

第二行开始具体输入地图信息，地图信息包括：
- 0为通畅的道路。
- 1为障碍物（且仅1为障碍物）。
- 2为小华或小为，地图中必定有且仅有两个（非障碍物）。
- 3为被选中的聚餐地点（非障碍物）。

**说明：**  

- 地图长宽为`m`和`n`，其中4 <= m,n <= 100。
- 聚餐的地点数量为`k`，其中1< k <= 100。

## 输出描述

可以两方都到达的聚餐地点的数量，行末无空格。

## 示例描述

### 示例一

**输入：**

```text
4 4 
2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0
```

**输出：**

```text
2
```

## 解题思路

**基本思路：** 使用广度优先搜索BFS求解。

1. 遍历所有地点，得到起始地点`start_spots`、聚会地点`end_spot`。
2. 使用广度优先搜索BFS：
    - 确定参数：当前地点的坐标`row`和`col`、聚会地点`end_spot`。
    - 终止条件：
        - 能到达聚会地点，返回True。
        - 当所有地点都访问过，当还是没有到达聚会地点，返回False
    - 递归处理：
        - 访问当前地点的上下左右各个地点，并依次存放到待遍历地点`queue`。
        - 如果超出边界，或者遇到障碍物，则继续遍历地点。
3. 如果两个起始地点都能达到聚会地点，则聚会地点的个数累加1。
4. 返回能到达的聚会地点的个数。

## 解题代码

```python
from collections import deque


def solve_method(arr):
    m = len(arr)
    n = len(arr[0])
    # 起始地点
    start_spots = []
    # 聚会地点
    end_spots = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 2:
                start_spots.append((i, j))
            elif arr[i][j] == 3:
                end_spots.append((i, j))
    count = 0

    def bfs(row, col, end_spot):
        # 待遍历的地点
        queue = deque([(row, col)])
        # 已访问的地点
        visited = {(row, col)}
        while queue:
            r, c = queue.popleft()

            # 能到达聚会地点，返回True
            if (r, c) == end_spot:
                return True
            # 访问上下左右的地点
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # 如果超出边界，或者遇到障碍物，则继续遍历
                if not (0 <= nr < m and 0 <= nc < n) or arr[nr][nc] == 1:
                    continue
                if (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        # 当所有地点都访问过，当还是没有到达聚会地点，返回False
        return False

    for end_spot in end_spots:
        if all(bfs(start_spot[0], start_spot[1], end_spot) for start_spot in start_spots):
            count += 1

    return count


if __name__ == '__main__':
    arr = [[2, 1, 0, 3],
           [0, 1, 2, 1],
           [0, 3, 0, 0],
           [0, 0, 0, 0]]
    assert solve_method(arr) == 2
```

