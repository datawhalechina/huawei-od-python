# 154火星改造

## 题目描述

2030年，人类通过对火星的大气进行宜居改造分析，使得火星已在理论上具备人类宜居的条件； 

由于技术原因，无法一次性将火星大气全部改造，只能通过局部处理形式；

 假设将火星待改造的区域为`row*column`的网格Q，每个网格有3个值，宜居区、可改造区、死亡区，使用`YES、NO、NA`代替：

`YES` 表示该网格已经完成大气改造； 

`NO`表示该网格未进行改造，后期可进行改造；

`NA`表示死亡区，不作为判断是否改造完成的宜居，无法穿过；

初始化下，该区域可能存在多个宜居区，并且每个宜居区能同时在每个太阳日单位向上下左右四个方向的相邻格子进行扩散，自动将4个方向相邻的真空区改造成宜居区；

请计算这个待改造区域的网格中，可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回-1。

## 输入描述

输入 输入 `row*column`个网格数据，每个网格值枚举值如下：`YES,NO,NA`

```
YES YES NO
NO NO NO
NA NO YEA
```



## 输出描述

可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回-1

## 示例描述

### 示例一

**输入：**

```text
YES YES NO
NO NO NO
NA NO YEA
```

**输出：**

```text
2
```

## 解题思路

使用广度优先搜索（BFS）的思想，首先统计初始宜居区和待改造区的数量。然后将初始宜居区加入BFS队列，并标记为已访问。在每一轮BFS中，遍历队列中的所有宜居区，对每个宜居区的四个方向上的待改造区进行改造，并将改造后的宜居区加入队列。同时更新待改造区的数量和天数。如果待改造区数量为0，则已经全部变成宜居区，返回天数。如果BFS结束后仍有待改造区，表示无法将待改造区全部变成宜居区，返回-1。

## 解题代码

```python
from collections import deque

def reconstruct_mars_grid(grid):
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    
    # 统计初始宜居区和待改造区的数量
    inhabited_count = 0
    to_be_reconstructed_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "YES":
                inhabited_count += 1
            elif grid[i][j] == "NO":
                to_be_reconstructed_count += 1
    
    # 如果待改造区数量为0，则已经全部变成宜居区，返回0
    if to_be_reconstructed_count == 0:
        return 0
    
    # 初始化BFS队列和访问标记数组
    queue = deque()
    visited = [[False] * cols for _ in range(rows)]
    
    # 将初始宜居区加入队列，并标记为已访问
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "YES":
                queue.append((i, j))
                visited[i][j] = True
    
    # 定义四个方向的偏移量
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    days = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols and not visited[nx][ny]:
                    if grid[nx][ny] == "NO":
                        # 将待改造区改造成宜居区
                        grid[nx][ny] = "YES"
                        to_be_reconstructed_count -= 1
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        days += 1
        
        # 如果待改造区数量为0，则已经全部变成宜居区，返回天数
        if to_be_reconstructed_count == 0:
            return days
    
    # 如果无法将待改造区全部变成宜居区，返回-1
    return -1

# 读取输入
grid = []
while True:
    try:
        row = input().split()
        if not row:
            break
        grid.append(row)
    except EOFError:
        break

# 调用函数计算可改造区是否能全部变成宜居区，以及改造的太阳日天数
result = reconstruct_mars_grid(grid)

# 输出结果
print(result)def solve_method(lights):
    lights_list = []
    for light in lights:
        id = light[0]
        x1 = light[1]
        y1 = light[2]
        x2 = light[3]
        y2 = light[4]
        # id, x坐标的平均值, y坐标的平均值, 灯高半径
        lights_list.append([id, (x1 + x2) // 2, (y1 + y2) // 2, (y2 - y1) // 2])

    # 将灯按行粗排
    lights_list.sort(key=lambda x: x[2])

    result = []

    # 设置每一行的起始索引
    row_start_index = 0
    # 先使用第1行第1个作为基准灯
    for i in range(1, len(lights_list)):
        # 高低偏差超过灯高度的一半
        if lights_list[i][2] - lights_list[row_start_index][2] > lights_list[row_start_index][3]:
            # 把之前的灯按x坐标排序，并存入结果列表中
            lights_list[row_start_index:i] = sorted(lights_list[row_start_index:i], key=lambda x: x[1])
            result.extend([light[0] for light in lights_list[row_start_index:i]])
            # 记录新一行对应的灯位置
            row_start_index = i

    # 把该行剩余的灯全部加入到结果列表中
    lights_list[row_start_index:] = sorted(lights_list[row_start_index:], key=lambda x: x[1])
    result.extend([light[0] for light in lights_list[row_start_index:]])

    return result
```

