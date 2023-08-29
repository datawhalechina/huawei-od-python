# 154 火星改造、宜居星球改造计划

## 题目描述

2030年，人类通过对火星的大气进行宜居改造分析，使得火星已在理论上具备人类宜居的条件。由于技术原因，无法一次性将火星大气全部改造，只能通过局部处理形式。

假设将火星待改造的区域为`row*column`的网格，每个网格有3个值：宜居区、可改造区、死亡区，使用`YES`、`NO`、`NA`代替，其中：
- `YES`表示该网格已经完成大气改造。 
- `NO`表示该网格未进行改造，后期可进行改造。
- `NA`表示死亡区，不作为判断是否改造完成的宜居，无法穿过。

初始化下，该区域可能存在多个宜居区，并且每个宜居区能同时在每个太阳日单位向上下左右四个方向的相邻格子进行扩散，自动将4个方向相邻的真空区改造成宜居区。

请计算这个待改造区域的网格中，可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回-1。

## 输入描述

输入`row*column`个网格数据，每个网格值枚举值如下：`YES`、`NO`、`NA`，其中1 <= row,column <= 8。

## 输出描述

可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回-1

## 示例描述

### 示例一

**输入：**

```text
YES YES NO
NO NO NO
YES NO NO 
```

**输出：**

```text
2
```

**说明：**

经过2个太阳日，完成宜居改造。

### 示例二

**输入：**

```text
YES NO NO NO
NO NO NO NO
NO NO NO NO
NO NO NO NO
```

**输出：**

```text
6
```

**说明：**

经过6个太阳日，完成宜居改造。

### 示例三

**输入：**

```text
NO NA
```

**输出：**

```text
-1
```

**说明：**

无改造初始条件，无法进行改造。

### 示例四

**输入：**

```text
YES NO NO YES
NO NO YES NO
NO YES NA NA
YES NO NA NO
```

**输出：**

```text
-1
```

**说明：**

右下角的区域，被周边三个死亡区挡住，无法实现改造。

## 解题思路

**基本思路：** 使用广度优先搜索BFS求解。

1. 遍历每一个区域，统计已经完成大气改造的区域的数量`count`，将坐标加入到已经访问过的区域的位置列表`visited`，将坐标待处理的区域`queue`，将。
2. 使用广度优先搜索，遍历可居住区域：
    - 终止条件：如果都访问了，退出循环。
    - 遍历处理：将已改造的区域的上下左右进行扩散，天数加1，并加入已经访问过的区域的位置列表中。
3. 检查是否所有的`NO`区域都被转化成`YES`，如果还存在，则返回-1。
4. 返回结果，即改造的太阳日天数。
   
## 解题代码

```python
def solve_method(grid):
    rows, cols = len(grid), len(grid[0])
    # 已经访问过的区域的位置
    visited = set()
    # 待处理的区域
    queue = []
    days = 0
    # 当前可居住区域的数量
    count = 0

    # 将所有初始的YES区域加入队列
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'YES':
                queue.append((i, j))
                visited.add((i, j))
                count += 1

    # 使用BFS扩展可居住区域
    while queue and len(visited) != rows * cols:
        days += 1
        size = len(queue)
        for _ in range(size):
            x, y = queue.pop(0)
            count -= 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'NO' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    count += 1

        if count == 0:
            break

    # 检查是否所有的NO区域都被转化成YES
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'NO' and (i, j) not in visited:
                return -1

    return days


if __name__ == '__main__':
    grid = [["YES", "YES", "NO"],
            ["NO", "NO", "NO"],
            ["YES", "NO", "NO"]]
    assert solve_method(grid) == 2

    grid = [["YES", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"]]
    assert solve_method(grid) == 6

    grid = [["NO", "NA"]]
    assert solve_method(grid) == -1

    grid = [["YES", "NO", "NO", "YES"],
            ["NO", "NO", "YES", "NO"],
            ["NO", "YES", "NA", "NA"],
            ["YES", "NO", "NA", "NO"]]
    assert solve_method(grid) == -1


if __name__ == '__main__':
    grid = [["YES", "YES", "NO"],
            ["NO", "NO", "NO"],
            ["YES", "NO", "NO"]]
    assert solve_method(grid) == 2

    grid = [["YES", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"],
            ["NO", "NO", "NO", "NO"]]
    assert solve_method(grid) == 6

    grid = [["NO", "NA"]]
    assert solve_method(grid) == -1

    grid = [["YES", "NO", "NO", "YES"],
            ["NO", "NO", "YES", "NO"],
            ["NO", "YES", "NA", "NA"],
            ["YES", "NO", "NA", "NO"]]
    assert solve_method(grid) == -1
```

